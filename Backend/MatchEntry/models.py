from django.db import models
import random

def getMBTI(responses: dict):
    
    def getLetter(value, a, b):
        if value == 3:
            return a
        elif value == -3:
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
    
    print(mbti)
    return ''.join(mbti)

def MBTIQuestions(): # THEIR ID WILL ALWAYS BE 0, 1, 2, 3
    return [
        {
            "question": "I prefer trying new and unfamiliar foods over sticking to what I know",
            "type": "choice",
            "id": 0,
            "choices": [
                # P: Embraces new experiences
                {"text": "Agree", "value": -3},
                # J: Sticks to known comfort
                {"text": "Disagree", "value": 3}
            ]
        },
        {
            "question": "I prefer focusing on the big picture rather than specific details when planning",
            "type": "choice",
            "id": 1,
            "choices": [
                {"text": "Agree", "value": -3},      # N: Big picture focused
                {"text": "Disagree", "value": 3}     # S: Detail-oriented
            ]
        },
        {
            "question": "I prefer one-on-one conversations over group discussions",
            "type": "choice",
            "id": 2,
            "choices": [
                {"text": "Agree", "value": -3},      # I: Energy from depth
                {"text": "Disagree", "value": 3}     # E: Group preference
            ]
        },
        {
            "question": "Personal fulfillment is more important than financial success in a career",
            "type": "choice",
            "id": 3,
            "choices": [
                {"text": "Agree", "value": -3},      # F: Value-based choices
                # T: Objective/financial criteria
                {"text": "Disagree", "value": 3}
            ]
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
            "min": {"text": "Strongly Agree", "value": -3},
            "max": {"text": "Strongly Disagree", "value": 3}
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
            "min": {"text": "Strongly Agree", "value": -3},
            "max": {"text": "Strongly Disagree", "value": 3}
        }
    ]

def controversialQuestion():
    return [
        {
            "question": "I think abortion should be legal.",
            "type": "slider",
            "id": 9,
            "min": {"text": "Strongly Agree", "value": -3},
            "max": {"text": "Strongly Disagree", "value": 3}
        },
        {
            "question": "Having equality policies create new inequalities.",
            "type": "slider",
            "id": 10,
            "min": {"text": "Strongly Agree", "value": -3},
            "max": {"text": "Strongly Disagree", "value": 3}
        },
        {
            "question": "The moon landing is a hoax.",
            "type": "slider",
            "id": 11,
            "min": {"text": "Strongly Agree", "value": -3},
            "max": {"text": "Strongly Disagree", "value": 3}
        }
    ]

def additionalQuestions():
    return [
        {
            "question": "If a hostile homeless guy with a knife confronted me, I will try to resolve it without physical violence.",
            "type": "slider",
            "id": 12,
            "min": {"text": "Strongly Agree", "value": -3},
            "max": {"text": "Nah I'll cook them 🤛", "value": 3}
        },
        {
            "question": "If my concentration didn't make as much money, I would've done something else I loved.",
            "type": "slider",
            "id": 13,
            "min": {"text": "Strongly Agree", "value": -3},
            "max": {"text": "Strongly Disagree", "value": 3}
        },
        {
            "question": "I love to gossip about other people.",
            "type": "slider",
            "id": 14,
            "min": {"text": "Strongly Agree", "value": -3},
            "max": {"text": "Strongly Disagree", "value": 3}
        },
        {
            "question": "The world is ending tomorrow, what are you going to do with your remaining time.",
            "type": "choice",
            "id": 15,
            "choices": [
                {"text": "Hangout with my friends/families one last time.", "value": -2},
                {"text": "Try things I have never done before, both legal and illegal.", "value": -1},
                {"text": "Commit crimes.", "value": 1},
                {"text": "Scroll reels for the last time 😩", "value": 2}
            ]
        },
        {
            "question": "Are you freaky?",
            "type": "slider",
            "id": 16,
            "min": {"text": "Very 😝", "value": -3},
            "max": {"text": "No I am normal", "value": 3}
        },
        {
            "question": "I believe I can win in physical fights even against stronger opponents, just because they are facing me.",
            "type": "slider",
            "id": 17,
            "min": {"text": "OFCC", "value": -3},
            "max": {"text": "Nah I'd get cooked 😭", "value": 3}
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
            "min": {"text": "I rizz them all up", "value": -3},
            "max": {"text": "I'm cooked 💀", "value": 3}
        }
    ]

def getQuestions():
    questions = MBTIQuestions() + viewpointQuestions() + controversialQuestion() + additionalQuestions()
    random.shuffle(questions)
    return questions

# Create your models here.
class MatchEntry(models.Model):
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.EmailField()
    mbti = models.CharField(max_length=4)
    embedding = models.JSONField(default=list)
    summary = models.TextField()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Match Entries"
