from django.urls import include, path
from rest_framework.routers import DefaultRouter 
from . import views

router = DefaultRouter()
router.register('', views.UserViewSet) 

urlpatterns = [
    path('', include(router.urls)) # 자동으로 url 생성
]