from django.shortcuts import render
from blogs.models import Blog
from blogs.models import Category

def index_view(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})