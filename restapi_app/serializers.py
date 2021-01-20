from rest_framework import serializers, viewsets
from .models import User

class RestSerializer(serializers.HyperlinkedModelSerializer): # HyperlinkedModelSerializer 상속 # 통신할 모델 설정
    class Meta:
        model = User
        fields = ('user_id', 'name', 'age') # 데이터 필드 설정 ## fields = '__all__'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RestSerializer