from django.shortcuts import render

def student_info(request):
    students = [
        {'Name': 'Alice', 'Marks': 85, 'Status': 'Pass'},
        {'Name': 'Bob', 'Marks': 78, 'Status': 'Pass'}, 
        {'Name': 'Charlie', 'Marks': 92, 'Status': 'Pass'}, 
        {'Name': 'Eva', 'Marks': 45, 'Status': 'Fail'},
    ]
