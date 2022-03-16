from .models import PostList
from .serializers import PostListSerializer
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView


class PostCreate(ListCreateAPIView):
    queryset = PostList.objects.all()
    serializer_class = PostListSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = PostList.objects.all()
    serializer_class = PostListSerializer
