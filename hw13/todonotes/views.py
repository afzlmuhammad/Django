from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes((AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)

    if form.is_valid():
        form.save()
        return Response(
            "Account created successfully",
            status=status.HTTP_201_CREATED
        )

    return Response(
        form.errors,
        status=status.HTTP_400_BAD_REQUEST
    )
    
    
    
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response(
            {'error': 'Please provide username and password'},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticate(username=username, password=password)

    if not user:
        return Response(
            {'error': 'Invalid Credentials'},
            status=status.HTTP_404_NOT_FOUND
        )

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'username': user.username,
        'token': token.key
    }, status=status.HTTP_200_OK)
    

from .models import Note

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_note(request):

    title = request.data.get('title')
    message = request.data.get('message')

    if not title or not message:
        return Response(
            {'error': 'Title and message are required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    note = Note.objects.create(
        user=request.user,
        title=title,
        message=message
    )

    return Response(
        {'message': 'Note added successfully', 'id': note.id},
        status=status.HTTP_201_CREATED
    )



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_notes(request):

    notes = Note.objects.filter(user=request.user)

    data = []

    for note in notes:
        data.append({
            'id': note.id,
            'title': note.title,
            'message': note.message
        })

    return Response(data)





