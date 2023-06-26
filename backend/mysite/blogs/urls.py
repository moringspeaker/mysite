from django.urls import path
from . import views
from .views import BlogDetailView

urlpatterns = [
        path('api/blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
        path('api/blogs/', views.BlogListView.as_view(), name='blog_api'),
    ]