from django.urls import path
from . import views

urlpatterns = [
    path('api/blogs/', views.BlogsAPIView.as_view(), name='blog_api'),
    path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
    ]