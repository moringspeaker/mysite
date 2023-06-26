from .models import Blog
from .models import Category
from .models import Collection
from rest_framework import generics
from collections import defaultdict
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogsSerializer

class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogsSerializer(blog)
        return Response(serializer.data)

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer  # replace this with your actual serializer

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

