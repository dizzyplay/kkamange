from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentSerializer, CommentCreateSerializer

from comment.models import Comment
from blog.models import Post


class ListComment(APIView):
    def get(self, request, post_id):
        comment = Comment.objects.filter(post=post_id)
        serializer = CommentSerializer(comment, many=True)

        return Response(serializer.data)

    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        user = request.user
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                post = post,
                user = user
            )
        return Response(serializer.data)


comment_list = ListComment.as_view()