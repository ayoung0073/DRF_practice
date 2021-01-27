from django.shortcuts import render

from rest_framework import viewsets # 기본 CRUD 만들자
from .models import User
from .serializers import UserSerializer

class BlogViewSet(viewsets.ModelViewSet): # viewsets.ModelViewSet을 상속하고 반드시 queryset과 serializer_class 명시
    queryset = User.objects.all()
    serializer_class = UserSerializer