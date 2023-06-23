from .models import Blog
from .models import Category
from .models import Collection
from rest_framework.pagination import LimitOffsetPagination
from .serializers import BlogsSerializer
from rest_framework import generics
from rest_framework.response import Response
from collections import defaultdict



class BlogsAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer
    pagination_class = LimitOffsetPagination
    pagination_class.default_limit = 5

    def format_created_date(self, blog):
        return blog.formatted_created_date()

    def list(self, request, *args, **kwargs):
        blogs = self.paginate_queryset(self.queryset)

        formatted_blogs = []
        for blog in blogs:
            formatted_blog = self.format_created_date(blog)
            formatted_blogs.append(formatted_blog)

        serializer = self.get_serializer(formatted_blogs, many=True)
        return self.get_paginated_response(serializer.data)




class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer  # replace this with your actual serializer

    def list(self, request, *args, **kwargs):
        categories = Category.objects.all()
        data = {}

        for category in categories:
            collection_groups = defaultdict(list)
            blogs = Blog.objects.filter(category=category)

            for blog in blogs:
                if blog.collection is None:
                    default_collection, _ = Collection.objects.get_or_create(
                        name="default",
                        category=category
                    )
                    collection_groups[default_collection.name].append({
                        'blog': blog,
                        'created_date_format': blog.formatted_created_date()
                    })
                else:
                    collection_groups[blog.collection.name].append({
                        'blog': blog,
                        'created_date_format': blog.formatted_created_date()
                    })

            data[category.name] = collection_groups

        return Response(data)




