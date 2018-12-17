from blog.models import Post
from comment.api.serializers import CommentSerializer

from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'nickname', 'title', 'content', 'photo', 'thumbnail', 'short_date', 'comment_count', 'comments']


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'content','photo','thumbnail']



