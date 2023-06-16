from django.urls import path
from user.views import login_view
from user.views import register
from . import views

urlpatterns = [
    path("", views.index_view, name="homepage"),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
]