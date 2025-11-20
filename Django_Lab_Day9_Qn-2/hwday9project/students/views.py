from django.shortcuts import render

def student_list(request):
    students = ['Alice', 'Bob', 'Charlie']
    return render(request, 'students/student_list.html', {'students': students})