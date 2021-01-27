from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer): # HyperlinkedModelSerializer 상속 # 통신할 모델 설정
    class Meta:
        model = User
        fields = ('user_id', 'name', 'age') # 데이터 필드 설정 ## fields = '__all__'
