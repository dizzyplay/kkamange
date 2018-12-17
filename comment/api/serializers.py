from rest_framework import serializers
from comment.models import Comment


class ChildCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['pk', 'nickname', 'post', 'content', 'short_date', 'parent']


class CommentSerializer(serializers.ModelSerializer):
    children = ChildCommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = ['pk', 'nickname', 'post', 'content', 'short_date', 'children']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']
