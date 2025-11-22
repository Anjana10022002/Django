from django.shortcuts import render, redirect
from .forms import studentform
from .models import student_record

def student_list(request):
    

def add_student(request):
    form = studentform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'add_student.html', {"students":students})