from rest_framework import serializers
from .models import Post, CustomUser, UserProfile

        
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


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('address', 'country', 'city', 'zip')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = CustomUser
        fields = ('url','first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zip = profile_data.get('zip', profile.zip)
        profile.save()

        return instance
