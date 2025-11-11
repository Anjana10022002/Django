from django.http import HttpResponse
def changeGreeting(request):
    return HttpResponse('Hello World')