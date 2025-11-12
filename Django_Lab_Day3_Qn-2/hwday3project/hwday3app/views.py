from django.shortcuts import render

def student_info(request):
    students = [
        {'Name': 'Alice', 'Marks': 85, 'Status': 'pass'},
        {'Name': 'Bob', 'Marks': 78, 'Status': 'pass'}, 
        {'Name': 'Charlie', 'Marks': 92, 'Status': 'pass'}, 
        {'Name': 'Eva', 'Marks': 45, 'Status': 'fail'},
    ]
    student = {'students': students}
    return render(request, 'students.html', student)
