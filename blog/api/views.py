from django.core.paginator import Paginator

from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Post

from .serializers import PostSerializer


class PostAPIview(APIView):
    def get(self, request):
        page = request.GET.get('page',1)
        qs = Post.objects.all()
        paginator = Paginator(qs, 2)
        if int(page) > int(paginator.num_pages):
            return Response(None)
        qs = paginator.get_page(page)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    def get(self, request):
        post_id = request.GET.get('id')
        post = Post.objects.get(pk=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)


post_list = PostAPIview.as_view()

post_detail = PostDetailView.as_view()