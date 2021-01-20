from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import staic
from rest_framework import routers # router import

router = routers.DefaultRouter()
routers.register('restapi', views.Rest_main)

urlpatterns = [
    #path('admin/', admin.site.urls),
    url('api-auth/', include('rest_framework.urls')),
    url(r'^api/doc', get_swagger_view(title='Rest API Document')),
    url(r'^$', include(routers.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)