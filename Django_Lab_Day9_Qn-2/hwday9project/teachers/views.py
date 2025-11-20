from django.shortcuts import render

def teachers(request):
    teachers = [
        {"name": "Mr. Smith", "subject": "Math"},
        {"name": "Ms. Johnson", "subject": "English"},
        {"name": "Mr. Lee", "subject": "Science"},  
    ]