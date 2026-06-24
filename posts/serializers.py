from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'post_type', 'caption', 'video', 'image', 'likes_count', 'created_at']

    def get_likes_count(self, obj):
        return obj.likes.count()