from django.shortcuts import render, redirect

def student_list(request):
    students = ['Alice', 'Bob', 'Charlie']
    return render(request, 'students/student_list.html', {'students': students})

def home(request):
    return render(request, 'students/home.html')

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)
        return redirect("student_list")
    return render(request, 'students/form.html')    