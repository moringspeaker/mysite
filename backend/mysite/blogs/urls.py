from django.urls import path
from . import views
from .views import BlogDetailView

urlpatterns = [
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("blogs/", views.BlogListView.as_view(), name="blog_api"),
    path("blogwrite", views.BlogCreateView.as_view(), name="blog_create_api"),
    path("categories/", views.CategoryListView.as_view(), name="category_api"),
    path("collections/", views.CollectionListView.as_view(), name="collection_api"),
]
