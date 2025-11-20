from django.shortcuts import render

def student_list(request):
    students = [
        {'name': 'Alice', 'age': 20},
        {'name': 'Bob', 'age': 22},
        {'name': 'Charlie', 'age': 23},
    ]
    return render(request, 'students/student_list.html', {'students': students})