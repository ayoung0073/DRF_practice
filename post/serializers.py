from rest_framework import serializers
from .models import Post, Comment
from user.models import User
from user.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostListSerializer(serializers.ModelSerializer): 
    writer = serializers.SerializerMethodField()
    comment = CommentSerializer(many=True, read_only=True) # serializers.SerializerMethodField() #CommentSerializer(many=True, read_only=True)
    # comments -> comment 로 수정 O

    class Meta:
        model = Post
        fields =  ('id', 'writer', 'title', 'content', 'comment') # '__all__' # ('writer', 'title', 'content') # 데이터 필드 설정 ## fields = '__all__'
        read_only_fields = ['title'] # 읽기전용 필드

    def get_writer(self, instance):
        return User.objects.get(name=instance.writer.name).user_id
    
class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = ['writer', 'title', 'content']

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['writer', 'post', 'content']

