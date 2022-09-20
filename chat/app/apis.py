from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from .permissions import IsAdmin


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.order_by('created_date')
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

