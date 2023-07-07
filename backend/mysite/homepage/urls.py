from django.urls import path
from . import views

urlpatterns = [
    # path("", views.index_view, name="homepage"),
    # path('login/', login_view, name='login'),
    # path('register/', register, name='register'),
    path("api/homepage/", views.homepage, name="homepage_api"),
]
