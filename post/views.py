from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer


# Create your views here.


class PostApiView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostModelViewSet(APIView):
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'success': True,
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass


class DetailPostApiView(APIView):
    def get(self, request,pk, format=None):
        posts = Post.objects.get(id=pk)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def put(self, request,pk):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        pass

    def delete(self, request, format=None):
        pass
