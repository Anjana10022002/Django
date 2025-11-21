from django.shortcuts import render

def add_student(request):
    return render(request, "add_student.html")

