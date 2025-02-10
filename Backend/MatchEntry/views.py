from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError, HttpResponseForbidden
from MatchEntry.models import getQuestions, maxScore, getMBTI, MatchEntry
from scipy.optimize import linear_sum_assignment
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import requests
from dotenv import load_dotenv
import os
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading
import numpy as np
import random
import time

load_dotenv()
LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
APIKEY = os.getenv("APIKEY")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # Use 465 for SSL

GMAIL_USER = os.getenv("EMAIL")
GMAIL_PASSWORD = os.getenv("PASSWORD")

FRONTEND_URL = os.getenv("FRONTEND_URL")

BASE_DIR = os.getcwd()

def send_email_async(email_template, title, replaces:dict, receiver_email):
    try:
        msg = MIMEMultipart()
        msg["From"] = GMAIL_USER
        msg["To"] = receiver_email
        msg["Subject"] = title
        
        with open(f"{BASE_DIR}/email_templates/{email_template}", "r", encoding="utf-8") as file:
            html_content = file.read()
            
        for key in replaces.keys():
            html_content = html_content.replace(key, replaces[key])
            
        # html_content = html_content.replace("{{LINK}}", f"{FRONTEND_URL}/result?uuid={entry.uuid}")
        msg.attach(MIMEText(html_content, "html"))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade to secure connection
        server.login(GMAIL_USER, GMAIL_PASSWORD)
        server.sendmail(GMAIL_USER, receiver_email, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {receiver_email}!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Create your views here.
@csrf_exempt
def allQuestions(request):
    try:
        if request.method == "GET":
            return JsonResponse(dict(questions=getQuestions()))
        else:
            return HttpResponseNotFound()
    except Exception as e:
        print(e)
        return HttpResponseServerError()
    
@csrf_exempt
def retrieveUser(request):
    try:
        if request.method == "GET":
            uuid = request.GET.get("uuid")
            return JsonResponse(MatchEntry.objects.get(uuid=uuid).serialize())
        else:
            return HttpResponseNotFound()
    except Exception as e:
        print(e)
        return HttpResponseServerError()
    
@csrf_exempt
def createEntry(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            fname = data["firstname"].lower().capitalize()
            lname = data["lastname"].lower().capitalize()
            email = data["email"]
            gender = data["gender"]
            classof = data["classof"]
            response = data["response"]
            perm_to_share = data["permission_to_share"]
            mbti = getMBTI(response)
            
            try:
                existin_entry = MatchEntry.objects.get(email=email)
                return HttpResponseForbidden()
            except MatchEntry.DoesNotExist:
                pass
            
            embedding = [0] * len(response.keys())
            uniqueness = [0] * len(response.keys())
            for id in response.keys():
                id = int(id)
                embedding[id] = response[str(id)]["value"]
                uniqueness[id] = abs(response[str(id)]["value"])
            
            score = np.linalg.norm(uniqueness) / maxScore()
            score *= 10000 # scale by 10,000 cause thats the max score
                
            res = None
            retries = 0
            
            while res == None and retries < 5:
                res = requests.post(LLM_ENDPOINT, 
                    headers={"Authorization": APIKEY},
                    json={
                        "prompt": f"""
                        Name: {fname} {lname}
                        MBTI: {mbti}
                        {response}\nGiven the response above, complete the following:
                        
                        - summary: Write a summary of their response to their questions. Plain text (One paragraph).
                        - insight: Talk about their personality from the data. Plain text (One paragraph).
                        - opp: Write how someone that is their opp would be like. Plain text (No limit).
                        *opp: Someone who is opposite from you, could be a hater. Do not include this definition in your response.
                        
                        Be funny and be witty, include some emojis. 
                        Use second person, as you are addressing to them directly.
                        Return your response in json format, with keys "summary", "insight", and "opp".
                        Output as raw json, This means NO CODE BLOCKS (ex: ```json).
                        """
                    }) 
                try:
                    res = json.loads(res.text)
                except:
                    res = None
                    retries += 1
                    print(f"Error parsing json, retrying {retries}/5")

            entry = MatchEntry(firstname=fname, lastname=lname, email=email, gender=gender, mbti=mbti, embedding=embedding, summary=res, score=score, permission_to_share=perm_to_share, classof=classof)
            entry.save()
        
            email_thread = threading.Thread(target=send_email_async, 
                args=('confirmation.html', 'OppMatch - Confirmation', {"{{NAME}}": entry.firstname, "{{LINK}}":  f"{FRONTEND_URL}/result?uuid={entry.uuid}"},
                      entry.email))
            email_thread.start()

            return HttpResponse(entry.uuid)
        else:
            return HttpResponseNotFound()
    except KeyError as e:
        return HttpResponseBadRequest()
    except Exception as e:
        print(e)
        return HttpResponseServerError()
    
@csrf_exempt
@login_required
def sendEngagementEmail(request):
    try:
        if request.method == "POST":
            users = MatchEntry.objects.all()
            total_users = len(users)
            estimated_time = total_users * 5  # 5 seconds per email

            # Background function for sending emails
            def send_emails():
                for user in users:
                    try:
                        send_email_async(
                            'engagement.html',
                            'Opposites in your AREA 😈!',
                            {"{{NAME}}": user.firstname, "{{COUNT_SIGNUPS}}": str(total_users)},
                            user.email
                        )
                        time.sleep(5)  # Wait 5 seconds per email to avoid rate limits
                    except Exception as e:
                        print(f"Error sending email to {user.email}: {e}")

            # Start the email sending process in a background thread
            email_thread = threading.Thread(target=send_emails)
            email_thread.daemon = True  # Ensure thread does not block app shutdown
            email_thread.start()

            # Return response immediately with estimated time
            return JsonResponse({
                "message": "Promo Emails are being sent in the background.",
                "total_recipients": total_users,
                "estimated_completion_time_seconds": estimated_time
            })
        else:
            return HttpResponseNotFound()
    except Exception as e:
        print(e)
        return HttpResponseServerError()
    
@csrf_exempt
@login_required
def sendUpdateEmail(request):
    try:
        if request.method == "POST":
            users = MatchEntry.objects.all()
            total_users = len(users)
            estimated_time = total_users * 5  # 5 seconds per email

            # Background function for sending emails
            def send_emails():
                for user in users:
                    # if no opp or acc disabled
                    if not user.opp or user.disabled: continue
                    try:
                        send_email_async(
                            'update.html',
                            'OppMatch 😈 - Update',
                            {
                                "{{INITIALS}}": f"{user.opp.firstname[0].capitalize()}{user.opp.lastname[0].capitalize()}", 
                                "{{LINK}}": f"{FRONTEND_URL}/result?uuid={user.uuid}",
                                "{{LINK_RAW}}": f"{FRONTEND_URL}/result?uuid={user.uuid}"
                            },
                            user.email
                        )
                        time.sleep(random.randint(1, 7))  # Wait 5 seconds per email to avoid rate limits
                    except Exception as e:
                        print(f"Error sending email to {user.email}: {e}")

            # Start the email sending process in a background thread
            email_thread = threading.Thread(target=send_emails)
            email_thread.daemon = True  # Ensure thread does not block app shutdown
            email_thread.start()

            # Return response immediately with estimated time
            return JsonResponse({
                "message": "Update Emails are being sent in the background.",
                "total_recipients": total_users,
                "estimated_completion_time_seconds": estimated_time
            })
        else:
            return HttpResponseNotFound()
    except Exception as e:
        print(e)
        return HttpResponseServerError()
    
    
@csrf_exempt
@login_required  # Ensures only admin users can access
def assign_opps(request):
    try:
        if request.method == "POST":

            print("Assigning opps...")
            
            entries = list(MatchEntry.objects.all())
            num_entries = len(entries)

            if num_entries % 2 != 0:
                return JsonResponse({"message": "Odd number of entries. Cannot form perfect pairs."}, status=400)

            similarity_matrix = np.zeros((num_entries, num_entries))

            for i in range(num_entries):
                for j in range(num_entries):
                    if i != j:  # Skip self-matching
                        similarity_matrix[i, j] = np.dot(entries[i].embedding, entries[j].embedding) / (
                            np.linalg.norm(entries[i].embedding) * np.linalg.norm(entries[j].embedding)
                        )
                        
            np.fill_diagonal(similarity_matrix, 1000)
            cost_matrix = similarity_matrix 
            # print(cost_matrix)
            # Solve the assignment problem using the Hungarian algorithm
            # minimum weight matching in bipartite
            row_ind, col_ind = linear_sum_assignment(cost_matrix)
            
            matched_pairs = []
            assigned_indices = set()

            for i in range(len(row_ind)):
                entry1 = entries[row_ind[i]]
                entry2 = entries[col_ind[i]]

                if row_ind[i] in assigned_indices or col_ind[i] in assigned_indices:
                    continue  # Skip already assigned entries

                entry1.opp = entry2
                entry2.opp = entry1
                entry1.save()
                entry2.save()

                matched_pairs.append((entry1.email, entry2.email, similarity_matrix[row_ind[i], col_ind[i]]))
                assigned_indices.add(row_ind[i])
                assigned_indices.add(col_ind[i])

            for match in matched_pairs:
                print(f"{match[0]} matched with {match[1]} | score: {match[2]}")

            return JsonResponse({"message": "Opps successfully assigned!"})
        
        return JsonResponse({"message": "Invalid request"}, status=400)
    except Exception as e:
        print(e)
        return HttpResponseServerError()