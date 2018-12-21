from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer, CommentCreateSerializer

from django.http.request import QueryDict

from comment.models import Comment
from blog.models import Post


class ListComment(APIView):

    def get(self, request):
        post_pk = request.GET.get('post_pk', 1)
        comment = Comment.objects.filter(post=post_pk)
        serializer = CommentSerializer(comment, many=True)

        return Response(serializer.data)

    def post(self, request):
        user_obj = request.user
        post_id = request.data['data']['post']
        qs = Post.objects.get(pk=post_id)
        c_qs = qs.comment_set.all()
        c_qs_serializer = CommentSerializer(c_qs, many=True)
        qd = QueryDict('', mutable=True)
        for k, v in request.data['data'].items():
            qd.update({k: v})
        serializer = CommentCreateSerializer(data=qd)
        if serializer.is_valid():
            serializer.save(
                user=user_obj,
            )
            return Response(c_qs_serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


comment_list = ListComment.as_view()
