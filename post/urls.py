from django.urls import include, path
from rest_framework.routers import DefaultRouter 
from . import views

# router = DefaultRouter()
# router.register('', views.PostViewSet.list)

urlpatterns = [
    path('', views.PostViewSet.post), # 자동으로 url 생성
    path('<int:post_id>', views.PostOneViewSet.post)
]