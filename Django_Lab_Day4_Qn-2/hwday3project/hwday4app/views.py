from django.shortcuts import render

def input_form(request):
    return render(request, 'index.html')

def result(request):
    if request.method == "POST":
        name = request.POST.get("name")
        color = request.POST.get("color")
        return render(request, "result.html", {
            "name": name,
            "color": color,
            "data": request.POST
        })
    return render(request, "index.html")
