from rest_framework import serializers
from .models import Swiper


class SwiperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swiper
        fields = ["id", "ENtitle", "CHtitle", "src"]
