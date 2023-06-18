from rest_framework import generics
from .models import Blog
from .models import Category
from rest_framework.pagination import LimitOffsetPagination
from .serializers import BlogsSerializer


class BlogsAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer
    pagination_class = LimitOffsetPagination
    # Set the default limit to 5
    pagination_class.default_limit = 5

class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer


