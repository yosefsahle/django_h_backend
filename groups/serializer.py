from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Group, GroupAdmin, GroupMember, GroupPost, GroupPostImage
from user.models import User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'group_profile_picture', 'group_name', 'group_description', 'group_type', 'group_bio', 'created_at']

class GroupAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupAdmin
        fields = ['id', 'group', 'user', 'user_role_on_group', 'created_at']

class GroupMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Use the detailed UserSerializer
    class Meta:
        model = GroupMember
        fields = ['user', 'joined_at']
    class Meta:
        model = GroupMember
        fields = ['id', 'user', 'group', 'joined_at']

class GroupPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupPostImage
        fields = ['id', 'image']

class GroupPostSerializer(serializers.ModelSerializer):
    images = GroupPostImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = GroupPost
        fields = ['id', 'group', 'user', 'title', 'description', 'posted_at', 'updated_at', 'images']

class GroupPostCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)
    
    class Meta:
        model = GroupPost
        fields = ['group', 'title', 'description', 'images']
    
    def create(self, validated_data):
        images = validated_data.pop('images')
        post = GroupPost.objects.create(**validated_data)
        for image in images:
            GroupPostImage.objects.create(post=post, image=image)
        return post
