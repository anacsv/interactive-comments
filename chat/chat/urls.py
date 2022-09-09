from rest_framework import routers
from django.urls import path, include
from app import apis

router = routers.DefaultRouter()
router.register(r'posts', apis.PostViewSet, 'posts')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))]