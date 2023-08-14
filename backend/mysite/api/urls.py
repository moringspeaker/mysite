from django.urls import path, include
from homepage import views as homepage_views
from user.views import UserRegViewSet
from blogs.views import (
    BlogDetailView,
    BlogListView,
    BlogCreateView,
    CategoryListView,
    CollectionListView,
    GetCollectioonandCategory,
)

urlpatterns = [
    path("homepage/", homepage_views.homepage, name="homepage_api"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),
    path("blogs/", BlogListView.as_view(), name="blog-list"),
    path("blogwrite/", BlogCreateView.as_view(), name="blog-create"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("collections/", CollectionListView.as_view(), name="collection-list"),
    path("user/", UserRegViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name="register"),
    path("collectcategory/", GetCollectioonandCategory.as_view(), name="collect_category"),
    ]


