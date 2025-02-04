from django.db import models
import random
from uuid import uuid4
import numpy as np

def getMBTI(responses: dict):
    
    def getLetter(value, a, b):
        if value >= 0:
            return a
        elif value < 0:
            return b
        else:
            return " "
    
    mbti = [" ", " ", " ", " "]
    
    for id in responses.keys():
        value = responses[id]["value"]
        id = int(id)
        
        if id == 0:
            mbti[3] = getLetter(value, "J", "P")
        elif id == 1:
            mbti[1] = getLetter(value, "S", "N")
        elif id == 2:
            mbti[0] = getLetter(value, "E", "I")
        elif id == 3:
            mbti[2] = getLetter(value, "T", "F")
    
    return ''.join(mbti)

def MBTIQuestions(): # THEIR ID WILL ALWAYS BE 0, 1, 2, 3
    return [
        {
            "question": "I prefer trying new and unfamiliar foods over sticking to what I know",
            "type": "slider",
            "id": 0,
            "min": {"text": "Disagree", "value": -3}, # P: Embraces new experiences
            "max": {"text": "Agree", "value": 3}# J: Sticks to known comfort
        },
        {
            "question": "I prefer focusing on the big picture rather than specific details when planning",
            "type": "slider",
            "id": 1,
            "min": {"text": "Disagree", "value": -3}, # N: Big picture focused
            "max": {"text": "Agree", "value": 3} # S: Detail-oriented
        },
        {
            "question": "I prefer one-on-one conversations over group discussions",
            "type": "slider",
            "id": 2,
            "min": {"text": "Disagree", "value": -3}, # I: Energy from depth
            "max": {"text": "Agree", "value": 3} # E: Group preference
        },
        {
            "question": "Personal fulfillment is more important than financial success in a career",
            "type": "slider",
            "id": 3,
            "min": {"text": "Disagree", "value": -3}, # F: Value-based choices
            "max": {"text": "Agree", "value": 3} # T: Objective/financial criteria
        }
    ]

def viewpointQuestions():
    return [
        {
            "question": "What's most important in life?",
            "type": "choice",
            "id": 4,
            "choices": [
                {"text": "Personal achievement and success 🤑", "value": -2},
                {"text": "Family and relationships 🤟", "value": -1},
                {"text": "Making a positive impact on society 💖", "value": 1},
                {"text": "Inner peace and contentment 😌", "value": 2}
            ]
        },
        {
            "question": "People are inherently good",
            "type": "slider",
            "id": 5,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        },
        {
            "question": "What's your view on personal responsibility?",
            "type": "choice",
            "id": 6,
            "choices": [
                {"text": "We are fully responsible for all outcomes", "value": -2},
                {"text": "We are mostly responsible with some exceptions", "value": -1},
                {"text": "Society shapes most outcomes", "value": 1},
                {"text": "Most things are beyond our control", "value": 2}
            ]
        },
        {
            "question": "What's your approach to life's problems?",
            "type": "choice",
            "id": 7,
            "choices": [
                {"text": "Problems are challenges to overcome", "value": -2},
                {"text": "Problems are learning opportunities", "value": -1},
                {"text": "Problems are part of life to accept", "value": 1},
                {"text": "Problems are tests from a higher power", "value": 2}
            ]
        },
        {
            "question": "Happiness is a choice we make.",
            "type": "slider",
            "id": 8,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        }
    ]

def controversialQuestion():
    return [
        {
            "question": "I think abortion should be legal.",
            "type": "slider",
            "id": 9,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        },
        {
            "question": "Having equality policies create new inequalities.",
            "type": "slider",
            "id": 10,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        },
        {
            "question": "The moon landing is a hoax.",
            "type": "slider",
            "id": 11,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        }
    ]

def additionalQuestions():
    return [
        {
            "question": "If a hostile homeless guy with a knife confronted me, I will try to resolve it without physical violence.",
            "type": "slider",
            "id": 12,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        },
        {
            "question": "If my concentration didn't make as much money, I would've done something else.",
            "type": "slider",
            "id": 13,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        },
        {
            "question": "I love to gossip about other people.",
            "type": "slider",
            "id": 14,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        },
        {
            "question": "The world is ending tomorrow, what are you going to do with your remaining time.",
            "type": "choice",
            "id": 15,
            "choices": [
                {"text": "Hangout with my friends/families one last time.", "value": -2},
                {"text": "Try things I have never done before, both legal and illegal.", "value": -1},
                {"text": "Learn the knowledge that I never got to learn.", "value": 1},
                {"text": "Scroll reels for the last time 😩", "value": 2}
            ]
        },
        {
            "question": "Are you freaky?",
            "type": "slider",
            "id": 16,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        },
        {
            "question": "I believe I can win in physical fights even against stronger opponents, just because they are facing me.",
            "type": "slider",
            "id": 17,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        },
        {
            "question": "Do you date to marry?",
            "type": "choice",
            "id": 18,
            "choices": [
                {"text": "Yes", "value": -1},
                {"text": "Sometimes", "value": 0},
                {"text": "No", "value": 1},
            ]
        },
        {
            "question": "I have a lot of rizz.",
            "type": "slider",
            "id": 19,
            "min": {"text": "Disagree", "value": -3},
            "max": {"text": "Agree", "value": 3}
        }
    ]

def getQuestions():
    questions = MBTIQuestions() + viewpointQuestions() + controversialQuestion() + additionalQuestions()
    random.shuffle(questions)
    return questions

CACHED_MAX_SCORE = None
def maxScore():
    global CACHED_MAX_SCORE
    if CACHED_MAX_SCORE == None:
        scores = []
        questions = getQuestions()
        for q in questions:
            if q["type"] == "slider":
                scores.append(q["max"]["value"])
            elif q["type"] == "choice":
                scores.append(max([c["value"] for c in q["choices"]]))
        CACHED_MAX_SCORE = np.linalg.norm(scores)
    return CACHED_MAX_SCORE
    
# Create your models here.
class MatchEntry(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('helicopter', 'AttackHelicopter'),
        ('non-binary', 'Non-binary'),
        ('transgender', 'Transgender'),
        ('genderqueer', 'Genderqueer'),
        ('genderfluid', 'Genderfluid'),
        ('agender', 'Agender'),
        ('other', 'Other'),
        ('prefer-not', 'Prefer not to say'),
    ]
    
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    mbti = models.CharField(max_length=4)
    gender = models.CharField(max_length=128, choices=GENDER_CHOICES)
    embedding = models.JSONField(default=list)
    score = models.IntegerField()
    summary = models.JSONField(default=dict)
    permission_to_share = models.BooleanField(default=False)
    uuid = models.CharField(max_length=128, default=uuid4)

    def __str__(self):
        return self.email
    
    def serialize(self):
        return {"firstname": self.firstname, "lastname": self.lastname, "mbti": self.mbti,
                "summary": self.summary, "score": self.score}
    
    class Meta:
        verbose_name_plural = "Match Entries"
