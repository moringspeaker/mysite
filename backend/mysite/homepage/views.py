# from django.shortcuts import render
# from blogs.models import Blog
# from blogs.models import Category

from rest_framework import generics
from .models import Swiper
from .serializers import SwiperSerializer

# Other views here...

class SwiperAPIView(generics.ListAPIView):  # use ListAPIView because we want a list of objects
    queryset = Swiper.objects.all()
    serializer_class = SwiperSerializer
