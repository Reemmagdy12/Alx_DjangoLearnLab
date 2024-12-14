from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField
    comments = CommentSerializer(many=True)
    class Meta:
        model = Post
        fields = '__all__'
