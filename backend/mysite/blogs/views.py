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

    # def list(self, request):
    #     data = {}
    #
    #     categories = Category.objects.all()
    #     data_category={}
    #     for category in categories:
    #         categroy_blogs = []
    #         data_category[category.name] = defaultdict(list)  # Create a default dictionary with category name
    #         blogs = Blog.objects.filter(category=category)
    #         for blog in blogs:
    #           if blog.collection is None:   # If the blog does not belong to any collection, add it to the category
    #             categroy_blogs.append(blog)
    #         data_category[category.name] = categroy_blogs
    #
    #     collections = Collection.objects.all()
    #     data_collection={}
    #     for collection in collections:
    #         collection_blog = []
    #         data_collection[collection.name] = defaultdict(list)
    #         blogs = Blog.objects.filter(collection=collection)
    #         for blog in blogs:
    #             collection_blog.append(blog)
    #         data_collection[collection.name] = collection_blog
    #
    #     data['category'] = data_category
    #     data['collection'] = data_collection
    #
    #     return Response(data)

    def list(self, request):
        data = {}

        categories = Category.objects.all()
        data_category = {}
        for category in categories:
            category_blogs = []
            data_category[category.name] = defaultdict(list)
            blogs = Blog.objects.filter(category=category)
            for blog in blogs:
                if blog.collection is None:
                    # use the serializer to transform the model instance to Python native datatypes.
                    serialized_blog = BlogsSerializer(blog).data
                    category_blogs.append(serialized_blog)
            data_category[category.name] = category_blogs

        collections = Collection.objects.all()
        data_collection = {}

        for collection in collections:
            collection_blogs = []
            data_collection[collection.name] = defaultdict(list)
            blogs = Blog.objects.filter(collection=collection)
            for blog in blogs:
                # use the serializer to transform the model instance to Python native datatypes.
                serialized_blog = BlogsSerializer(blog).data
                collection_blogs.append(serialized_blog)
            data_collection[collection.name] = collection_blogs
            data_collection[collection.name].append(collection.category.name)   #

        data['category'] = data_category
        data['collection'] = data_collection

        return Response(data)

