from django.core.paginator import Paginator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from blog.models import Post
from user.models import Profile

from .serializers import PostSerializer, PostCreateSerializer


class PostAPIview(APIView):

    def get(self, request):
        page = request.GET.get('page', 1)
        qs = Post.objects.all()
        paginator = Paginator(qs, 3)
        if int(page) > int(paginator.num_pages):
            return Response(status=status.HTTP_204_NO_CONTENT)
        qs = paginator.get_page(page)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        serializer = PostCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=user,
                nickname=Profile.objects.get(user=user).nickname
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data)


class PostDetailView(APIView):
    def get(self, request):
        post_id = request.GET.get('id')
        post = Post.objects.get(pk=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)


post_list = PostAPIview.as_view()

post_detail = PostDetailView.as_view()
