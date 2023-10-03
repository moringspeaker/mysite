from django.urls import path
from .views import UserRegViewSet

urlpatterns = [
    path("user/", UserRegViewSet.as_view({
        'post': 'create'
    }), name="register"),
]
