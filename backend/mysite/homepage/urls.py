from django.urls import path
from user.views import login_view
from . import views

urlpatterns = [
    path("", views.index_view, name="homepage"),
    path('login/', login_view, name='login'),
]