# from rest_framework import serializers
# from .models import Blog
#
# class BlogsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blog
#         fields = ['id', 'ENtitle','ENcontent','ENauthor','ENsummary','CHtitle','CHcontent','CHauthor','CHsummary','cover','created_date','category','collection']

from rest_framework import serializers
from .models import Blog

class BlogsSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'ENtitle', 'ENcontent', 'ENauthor', 'ENsummary', 'CHtitle', 'CHcontent', 'CHauthor',
                  'CHsummary', 'cover', 'created_date', 'collection', 'category', 'category_name']

    def get_category_name(self, obj):
        return obj.category.name
