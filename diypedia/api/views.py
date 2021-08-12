from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import *
from users.models import *

from .serializers import PostListSerializer, PostDetailSerializer, CategoryCreateSerializer, CategorySerializer


class PostListAPIview(APIView):
    def get(self, request):
        queryset = Post.objects.all()
        serializer_for_qs = PostListSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_qs.data)


class PostDetailAPIview(APIView):
    def get(self, request, pk):
        queryset = Post.objects.get(id=pk)
        serializer_for_qs = PostDetailSerializer(
            instance=queryset,
        )
        return Response(serializer_for_qs.data)


class CategoryListAPIview(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer_for_qs = CategorySerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_qs.data)


class CategoryCreateAPIview(APIView):
    def post(self, request):
        category = CategoryCreateSerializer(data=request.data)
        if category.is_valid():
            category.save()
        return Response(status=201)