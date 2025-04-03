from apps.blog.models import Post
from rest_framework import generics
from .serializers import PostSerializer

# ListCreateAPIView.
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    
# RetrieveDestroyAPIView
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
# class PostDetail(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    