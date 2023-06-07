from django.urls import path
from django.urls import include
from . import views


app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='user_login'),
]
