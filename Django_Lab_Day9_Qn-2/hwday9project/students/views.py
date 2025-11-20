from django.shortcuts import render

def student_list(request):
    students = ['Alice', 'Bob', 'Charlie']
    return render(request, 'students/student_list.html', {'students': students})

def home(request):
    return render(request, 'students/home.html')