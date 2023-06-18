from django.http import JsonResponse
from .models import Swiper
from blogs.models import Blog
from .serializers import SwiperSerializer
from blogs.serializers import BlogsSerializer
def homepage(request):
    blogs = Blog.objects.all()[:5]  # Get the latest 5 blogs
    swipers = Swiper.objects.all()  # Get all swipers

    blog_serializer = BlogsSerializer(blogs, many=True)
    swiper_serializer = SwiperSerializer(swipers, many=True)

    blog_data = blog_serializer.data
    swiper_data = swiper_serializer.data

    response_data = {
        'blogs': blog_data,
        'swipers': swiper_data,
    }

    return JsonResponse(response_data)
