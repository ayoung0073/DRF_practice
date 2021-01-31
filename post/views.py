from rest_framework import viewsets # 기본 CRUD 만들자
from .models import Post
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from my_user.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

class PostViewSet(APIView):

    @api_view(['GET', 'POST'])
    @permission_classes([IsAuthenticated])
    def post(request):
        print(request.user)
        if request.method == 'GET':
            queryset = Post.objects.all()
            serializer = PostListSerializer(queryset, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            #data = JSONParser().parse(request)
            serializer = PostCreateSerializer(data=request.data) # writer : 1(user의 id)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            else:
                print(serializer.error_messages)
                return JsonResponse(serializer.errors, status=400)

class PostOneViewSet(APIView):

    @api_view(['GET', 'PUT', 'DELETE'])
    @permission_classes([IsAuthenticated])
    def post(request, post_id): # urls : <int:post_id>
        try:
            post = Post.objects.get(pk=post_id) 
        except Post.DoesNotExist :
            # 해당 인스턴스가 존재하지 않을 경우
                return Response(
                    {
                        'error':
                        {
                            'code':404,
                            'message':'Post not found.'
                        }
                    }, status=404)

        if request.method == 'GET':
            serializer = PostListSerializer(post)
            return Response(serializer.data, status=200) # JsonResponse와 같음

        elif request.method == 'PUT':
            # request에서 data를 받으면, is_valid() 필수
            #data = JSONParser().parse(request)
            serializer = PostUpdateSerializer(post, data=request.data) # (전달할 인스턴스, 수정할 데이터)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400) # 잘못된 데이터 요청
        elif request.method == 'DELETE':
            post.delete()
            # 인스턴스 삭제 후, 204 NO CONTENT 리턴
            return Response(status=status.HTTP_204_NO_CONTENT)
            
                    
class CommentViewSet(APIView):

    @api_view(['GET', 'POST'])
    @permission_classes([IsAuthenticated])
    def comment(request):
        if request.method == 'GET':
            queryset = Comment.objects.all()
            serializer = CommentSerializer(queryset, many=True)
            return Response(serializer.data, status=200)

        elif request.method == 'POST': # 댓글 작성
            # {post":1, "content":"댓글 test"}
            #json_data = JSONParser().parse(request)

            data = {}
            data['writer'] = User.objects.get(username=request.user).id
            # 인증된 user을 writer로 설정
            data['post'] = request.data['post']
            data['content'] = request.data['content']

            serializer = CommentDetailSerializer(data=data) 
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            else:
                print(serializer.error_messages)
                return JsonResponse(serializer.errors, status=400)

class CommentOneViewSet(APIView):

    @api_view(['GET', 'PUT', 'DELETE'])
    @permission_classes([IsAuthenticated])
    def comment(request, comment_id): # urls : <int:post_id>
        try:
            comment = Comment.objects.get(pk=comment_id) 
        except Comment.DoesNotExist :
            # 해당 인스턴스가 존재하지 않을 경우
                return Response(
                    {
                        'error':
                        {
                            'code':404,
                            'message':'Comment not found.'
                        }
                    }, status=404)

        if request.method == 'GET':
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=200) # JsonResponse와 같음

        elif request.method == 'PUT':
            if User.objects.get(username=request.user) == comment.writer: # 객체 비교
                print('same')
                serializer = CommentUpdateSerializer(comment, data=request.data) # (전달할 인스턴스, 수정할 데이터)
                # request에서 data를 받으면, is_valid() 필수
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=200)
                return Response(serializer.errors, status=400) # 잘못된 데이터 요청
            else:
                return Response(
                    {
                        'error':
                        {
                            'code':400,
                            'message':'수정 권한이 없습니다.'
                        }
                    }, status=400)

        elif request.method == 'DELETE':
            if User.objects.get(username=request.user) == comment.writer: # 객체 비교
                comment.delete()
                # 인스턴스 삭제 후, 204 NO CONTENT 리턴
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(
                    {
                        'error':
                        {
                            'code':400,
                            'message':'삭제 권한이 없습니다.'
                        }
                    }, status=400)