from rest_framework import serializers
from .models import Post,PostImage,Comment

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id','image']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','user','post','comment','date']

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True,read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id','user', 'category', 'title', 'description', 'posted_at', 'images','comments']

class PostCreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(), write_only=True
    )

    class Meta:
        model = Post
        fields = ['category','title', 'description','images']
    
    def create(self,validated_data):
        images = validated_data.pop('images')
        post = Post.objects.create(**validated_data)
        for image in images:
            PostImage.objects.create(post=post,image=image)
        return post

