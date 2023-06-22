from rest_framework import generics
from .models import Blog
from .models import Category
from rest_framework.pagination import LimitOffsetPagination
from .serializers import BlogsSerializer
from django.http import JsonResponse

class BlogsAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogsSerializer
    pagination_class = LimitOffsetPagination
    # Set the default limit to 5
    pagination_class.default_limit = 5

class BlogDetailView(generics.RetrieveAPIView):

    def get_all_categories(self):
        return Category.objects.all()
    def get_blogs_by_category(self, category):
        return Blog.objects.filter(category=category)

    def return_all_blog(self):
        categories = self.get_all_categories()
        blogs = {}
        for category in categories:
            blogs[category.name] = self.get_blogs_by_category(category)

        return JsonResponse(blogs)




