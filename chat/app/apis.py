from app.models import Post
from django.contrib.auth.models import User
from app.serializers import PostSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from app.permissions import IsAdmin, IsSameUser

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('created_date')
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSameUser]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]
    
    