from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token 
from django.views.decorators.csrf import csrf_exempt
from .models import Note
from .serializers import NoteSerializer
from . import productForm

@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("Account created succesfully ", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUESTs)

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error':'please provide an username and password'}, status=status.HTTP_404_NOT_FOUND)
    user = authenticate(username = username, password = password)
    if not user:
        return Response({'error':'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'username': user.username}, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated))
def add_note(request):
    title = request.POST.get("title")
    message = request.POST.get("message")
    if not title or not message:
        return Response({'error':'Please enter both title and meaasge'}, status=status.HTTP_400_BAD_REQUEST)
    note = Note.objects.create(title=title, message=message)
    if not note:
        return Response({'error':'Invalid data'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'title':note.title, 'message':note.message},status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def note_list(request):
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)
    return Response(serializer.data)





csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def create_product(request):
    form = productForm(request.POST)
    if form.is_valid():
        product = form.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(form.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((AllowAny))


