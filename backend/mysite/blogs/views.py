from rest_framework import generics, status
from collections import defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog, Category, Collection
from .serializers import BlogsSerializer, CategorySerializer, CollectionSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.paginator import Paginator
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class BlogDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer



class BlogCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    def post(self, request, *args, **kwargs):
        category_name = request.data.get("category")
        category, created = Category.objects.get_or_create(
            name=category_name,
        )
        # Get or create the Collection only if provided
        collection_name = request.data.get("collection")
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

        if collection is not None:
            blog_data["collection"] = collection.id

        serializer = BlogsSerializer(data=blog_data)
        if self.request.user.is_superuser:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            else:
                print('invalid serializer')
                return Response(data=serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            raise PermissionError("Only superusers can create blog posts.")


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-created_date')
    serializer_class = BlogsSerializer  # replace this with your actual serializer

    def post(self, request):
        page_number = request.data.get('page', 1)
        paginator = Paginator(self.get_queryset(), 6)  # 6 blogs per page

        try:
            current_page_blogs = paginator.page(page_number)
        except Exception as e:
            print(e)
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
            data_collection[collection.name] = defaultdict(list)
            blogs = Blog.objects.filter(collection=collection)
            serialized_blogs = [BlogsSerializer(blog).data for blog in blogs]
            collection_data['blogs'] = serialized_blogs
            collection_data['category'] = collection.category.name

            data_collection[collection.name] = collection_data

        data["category"] = data_category
        data["collection"] = data_collection

        return Response(data)