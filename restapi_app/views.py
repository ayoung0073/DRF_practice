from django.shortcuts import render
from .serializers import RestSerializer # serializer 연동
from .models import User # model 연동
from rest_framework import viewsets # modelViewSet을 가져와서 연동

class Rest_main(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RestSerializer