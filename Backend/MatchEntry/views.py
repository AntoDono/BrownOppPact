from django.shortcuts import render
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from MatchEntry.models import getQuestions, getMBTI, MatchEntry
import json
from django.views.decorators.csrf import csrf_exempt

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
def createEntry(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body)
            fname = data["firstname"]
            lname = data["lastname"]
            email = data["email"]
            response = data["response"]
            mbti = getMBTI(response)
            
            embedding = [0] * len(response.keys())
            for id in response.keys():
                embedding[id] = response[id].value
                
            summary = ""
            
            entry = MatchEntry(firstname=fname, lastname=lname, email=email, mbti=mbti, embedding=embedding, summary=summary)
            entry.save()
            return HttpResponse()
        else:
            return HttpResponseNotFound()
    except KeyError as e:
        return HttpResponseBadRequest()
    except Exception as e:
        print(e)
        return HttpResponseServerError()