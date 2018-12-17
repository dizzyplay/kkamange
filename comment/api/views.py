from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer, CommentCreateSerializer

from comment.models import Comment
from blog.models import Post


class ListComment(APIView):
    def get(self, request):
        post_pk = request.GET.get('post_pk', 1)
        comment = Comment.objects.filter(post=post_pk)
        serializer = CommentSerializer(comment, many=True)

        return Response(serializer.data)

    def post(self, request):
        comment_obj = None
        post_pk = request.POST.get('post_pk')
        comment_pk = request.POST.get('comment_pk', None)
        if comment_pk is not None:
            comment_obj = Comment.objects.get(pk=comment_pk)
        post_obj = Post.objects.get(id=post_pk)
        user_obj = request.user
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                post=post_obj,
                user=user_obj,
                parent=comment_obj
            )
        return Response(serializer.data, status=status.HTTP_201_CREATED)


comment_list = ListComment.as_view()
