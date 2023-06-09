from .models import Blog
from .models import Category
from .models import Collection
from rest_framework import generics, status
from collections import defaultdict
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogsSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class BlogDetailView(APIView):
    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        serializer = BlogsSerializer(blog)
        return Response(serializer.data)


class BlogCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        category_name = request.data.get("category")
        category, created = Category.objects.get_or_create(
            name=category_name,
        )

        print(category)
        # Get or create the Collection only if provided
        collection_name = request.data.get("collection")
        print(collection_name)
        collection = None

        if collection_name:
            collection, created = Collection.objects.get_or_create(
                name=category_name,
                category=category,
            )
            # If the Collection already exists but its category is different from the current category, set the blog's category to the collection's category.
            if collection.category != category:
                category = collection.category

        blog_data = {
            "ENtitle": request.data.get("ENtitle"),
            "ENcontent": request.data.get("ENcontent"),
            "ENauthor": request.data.get("ENauthor"),
            "ENsummary": request.data.get("ENsummary"),
            "CHtitle": request.data.get("CHtitle"),
            "CHcontent": request.data.get("CHcontent"),
            "CHauthor": request.data.get("CHauthor"),
            "CHsummary": request.data.get("CHsummary"),
            "cover": request.data.get("cover"),
            "category": category.id,
        }

        # Only include 'collection' in blog_data if a collection exists
        if collection is not None:
            blog_data["collection"] = collection.id

        serializer = BlogsSerializer(data=blog_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            data_collection[collection.name].append(collection.category.name)  #

        data["category"] = data_category
        data["collection"] = data_collection

        return Response(data)


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        data = []
        for category in categories:
            data.append(category.name)
        return Response(data)


class CollectionListView(APIView):
    def get(self, request):
        collections = Collection.objects.all()
        data = []
        for collection in collections:
            data.append(collection.name)
        return Response(data)
