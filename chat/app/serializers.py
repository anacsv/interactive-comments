from rest_framework import serializers
from .models import Post
        
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','username','comment','created_date','parent_post','replies']
        read_only_fields = ['replies']
        
class PostSerializer(serializers.ModelSerializer):
    replies = ReplySerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id','username','comment','created_date','parent_post','replies']
        read_only_fields = ['replies']