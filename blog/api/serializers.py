from blog.models import Post
from user.models import Profile
from comment.serializers import CommentSerializer

from rest_framework.serializers import ModelSerializer


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'nickname', 'title', 'content', 'photo', 'thumbnail', 'created_at','comment_count']
