from django.urls import path, include
from homepage import views as homepage_views
from blogs import views as blogs_views
from user import views as user_views
from blogs.views import (
    BlogDetailView,
    BlogListView,
    BlogCreateView,
    CategoryListView,
    CollectionListView,
)
from user.views import SuperUserLoginView

urlpatterns = [
    path("homepage/", homepage_views.homepage, name="homepage_api"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("blogs/", BlogListView.as_view(), name="blog-list"),
    path("blogwrite/", BlogCreateView.as_view(), name="blog-create"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("collections/", CollectionListView.as_view(), name="collection-list"),
    path("superuser_login/",SuperUserLoginView.as_view(),name="superuser_login",),
    ]


