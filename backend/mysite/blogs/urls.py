from django.urls import path
from . import views
from .views import BlogDetailView

urlpatterns = [
    path("api/blogs/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("api/blogs/", views.BlogListView.as_view(), name="blog_api"),
    path("api/blogwrite", views.BlogCreateView.as_view(), name="blog_create_api"),
    path("api/categories/", views.CategoryListView.as_view(), name="category_api"),
    path("api/collections/", views.CollectionListView.as_view(), name="collection_api"),
]
