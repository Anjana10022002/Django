from django.shortcuts import render, redirect
from .forms import studentform
from .models import student_record

def student_list(request):
    student = student_record.objects.all()
    return render(request, 'student_list.html', {'students': student})

def add_student(request):
    form = studentform(request.POST)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'add_student.html', {"students": students})

def edit_students(request):
    student = student_record.objects.get(pk=id)
    if request.method == 'POST':
        form = studentform(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})