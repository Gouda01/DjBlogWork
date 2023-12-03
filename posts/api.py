from rest_framework.decorators import api_view
from .models import Post
from .serializer import PostSerializer
from rest_framework.response import Response
from rest_framework import generics



@api_view()
def post_list_api (request) :
    posts = Post.objects.all()
    data = PostSerializer(posts,many=True).data

    return Response({'data':data})

@api_view()
def post_detail_api (request,pk) :
    post = Post.objects.get(id=pk)
    data = PostSerializer(post).data

    return Response({'data':data})


class PostListApi(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
