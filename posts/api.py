from rest_framework.decorators import api_view
from .models import Post
from .serializer import PostSerializer
from rest_framework.response import Response


@api_view()
def post_list_api (request) :
    posts = Post.objects.all()
    data = PostSerializer(posts,many=True).data

    return Response({'data':data})