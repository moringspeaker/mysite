from rest_framework import serializers
from .models import Blog

class BlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'ENtitle','ENcontent','ENauthor','ENsummary','CHtitle','CHcontent','CHauthor','CHsummary','cover','created_date','category']
