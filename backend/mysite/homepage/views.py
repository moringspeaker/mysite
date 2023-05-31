from django.shortcuts import render
from .models import Blog
from .models import Category

def index_view(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blog': blogs})