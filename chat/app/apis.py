from .serializers import PostSerializer
from .models import Post
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(parent_post__isnull=True).order_by('created_date')
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
