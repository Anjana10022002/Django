from django.shortcuts import render

def teachers_list(request):
    teachers = ["Mr. Smith", "Ms. Johnson", "Mr. Lee"]
    return render(request, "teachers/teachers_list.html", {"teachers": teachers})
# def teachers_list(request):
#     teachers = Teacher.objects.all()
#     return render(request, "teachers/teachers_list.html", {"teachers": teachers})