from .models import Blog
from .models import Category
from .models import Collection
from rest_framework import generics, status
from collections import defaultdict
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog, Category, Collection
from .serializers import BlogsSerializer, CategorySerializer, CollectionSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.paginator import Paginator
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, ListAPIView
class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer

    # def get(self, request, pk):
    #     blog = get_object_or_404(Blog, pk=pk)
    #     serializer = BlogsSerializer(blog)
    #     return Response(serializer.data)


class BlogCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def check_blog_data(self,data):
        for key, value in data.items():
            if value is None or value == "":
                return False, key  # Returning the key as well to know which attribute was null
        return True, None

    def post(self, request, *args, **kwargs):
        category_name = request.data.get("category")
        category, created = Category.objects.get_or_create(
            name=category_name,
        )
        # Get or create the Collection only if provided
        collection_name = request.data.get("collection")
        collection = None
        print(collection_name)

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

        # check the data
        is_valid, invalid_key = self.check_blog_data(blog_data)
        print('1111111111')
        if not is_valid:
            print('invalid data')
            return response.Response(
                data={"message": f"Invalid data: {invalid_key} is null"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            if collection is not None:
                blog_data["collection"] = collection.id

            serializer = BlogsSerializer(data=blog_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print('invalid serializer')
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-created_date')
    serializer_class = BlogsSerializer  # replace this with your actual serializer

    def post(self, request):
        page_number = request.data.get('page', 1)
        paginator = Paginator(self.get_queryset(), 6)  # 6 blogs per page

        try:
            current_page_blogs = paginator.page(page_number)
        except EmptyPage:
            return Response({"error": "No results for this page."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(current_page_blogs, many=True)

        # You can construct your paginated response here:
        paginated_response = {
            'count': paginator.count,
            'num_pages': paginator.num_pages,
            'current_page': page_number,
            'results': serializer.data
        }

        return Response(paginated_response)

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CollectionListView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class GetCollectioonandCategory(APIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer  # replace this with your actual serializer

    def get(self, request):

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
            collection_data = {}
            collection_blogs = []
            data_collection[collection.name] = defaultdict(list)
            blogs = Blog.objects.filter(collection=collection)
            serialized_blogs = [BlogsSerializer(blog).data for blog in blogs]
            collection_data['blogs'] = serialized_blogs
            collection_data['category'] = collection.category.name

            data_collection[collection.name] = collection_data

        data["category"] = data_category
        data["collection"] = data_collection

        return Response(data)