from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Post
from comment.models import Comment
from .serializers import PostSerializer


class PostAPIview(APIView):
    def get(self, request):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    def get(self, request, post_pk):
        post = Post.objects.get(pk=post_pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


post_list = PostAPIview.as_view()

post_detail = PostDetailView.as_view()