from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from MatchEntry.models import getQuestions, maxScore, getMBTI, MatchEntry
import json
from django.views.decorators.csrf import csrf_exempt
import requests
from dotenv import load_dotenv
import os
import numpy as np

load_dotenv()
LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")
APIKEY = os.getenv("APIKEY")

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
            fname = data["firstname"]
            lname = data["lastname"]
            email = data["email"]
            gender = data["gender"]
            response = data["response"]
            perm_to_share = data["permission_to_share"]
            mbti = getMBTI(response)
            
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
                        
                        - summary: Write a summary of their response to their questions (One paragraph)
                        - insight: Talk about their personality from the data. (One paragraph)
                        - opp: Write how someone that is their opp would be like. (No limit)
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

            entry = MatchEntry(firstname=fname, lastname=lname, email=email, gender=gender, mbti=mbti, embedding=embedding, summary=res, score=score, permission_to_share=perm_to_share)
            entry.save()
            return HttpResponse(entry.uuid)
        else:
            return HttpResponseNotFound()
    except KeyError as e:
        return HttpResponseBadRequest()
    except Exception as e:
        print(e)
        return HttpResponseServerError()