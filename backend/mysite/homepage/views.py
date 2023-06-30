from django.http import JsonResponse
from .models import Swiper
from blogs.models import Blog
from .serializers import SwiperSerializer
from blogs.serializers import BlogsSerializer
def homepage(request):
    blogs = Blog.objects.order_by('-id')[:5]
    for blog in blogs:
        blog.created_time = blog.formatted_created_date()
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
