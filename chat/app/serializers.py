from rest_framework import serializers
from app.models import Post
from django.contrib.auth.models import User

from django.contrib.auth.hashers import make_password

        
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password', 'is_active', 'last_login','is_superuser']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'], validated_data['username'])
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        
        if 'password' in validated_data:
            instance.password = make_password(validated_data['password'], validated_data['username'])
        
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance