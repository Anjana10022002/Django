from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("Account created succesfully ", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUESTs)

@api_view(["GET"])
@permission_classes((AllowAny))
def login(request):
    username = request.data.get("username")
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error':'please provide an username and password'}, status=status.HTTP_404_NOT_FOUND)
    user = authenticate(username = username, password = password)
    if not user:
        return Response({'error':'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.