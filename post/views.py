from rest_framework import viewsets # 기본 CRUD 만들자
from .models import Post
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

class PostViewSet(APIView):

    @api_view(['GET', 'POST'])
    def post(request):
        if request.method == 'GET':
            queryset = Post.objects.all()
            serializer = PostListSerializer(queryset, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = PostCreateSerializer(data=data) # writer : 1(user의 id)
            print(data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            else:
                print(serializer.error_messages)
                return JsonResponse(serializer.errors, status=400)
