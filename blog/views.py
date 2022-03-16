from django.shortcuts import render
from rest_framework.views import APIView
from .models import PostList
from .serializers import PostListSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class PostListView(APIView):

    def get(self, request):
        queryset = PostList.objects.all()
        serializer = PostListSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
