from django.urls import path
from . import views

urlpatterns = [
    # path('blogs/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail'),
        path('api/blogs/', views.BlogListView.as_view(), name='blog_api'),
    ]