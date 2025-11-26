from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, AllowwAny
from rest_framework.response import response
from django.contrib.auth.forms import UserCreationForm

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return response("Account created succesfully ", status=status.HTTP_201_CREATED)
    return response(form.errors, status=status.HTTP_400_BAD_REQUESTs)
