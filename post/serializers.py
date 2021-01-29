from rest_framework import serializers
from .models import Post
from user.models import User
from user.serializers import UserSerializer

class PostListSerializer(serializers.ModelSerializer): # HyperlinkedModelSerializer 상속 # 통신할 모델 설정
    writer = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__' #('writer', 'title', 'content') # 데이터 필드 설정 ## fields = '__all__'
        read_only_filds = 'title' # 읽기전용 필드

    def get_writer(self, obj):
        return User.objects.get(name=obj.writer.name).user_id

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Post
        fields = ['writer', 'title', 'content']


