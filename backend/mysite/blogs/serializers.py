from rest_framework import serializers
from .models import Blog, Category, Collection


class BlogsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    CHsummary = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "ENtitle",
            "ENcontent",
            "ENauthor",
            "ENsummary",
            "CHtitle",
            "CHcontent",
            "CHauthor",
            "CHsummary",
            "cover",
            "created_date",
            "collection",
            "category",
        ]

    def get_category_name(self, obj):
        return obj.category.name

class CollectionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = Collection
        fields = [
            "id",
            "name",
            "category_name",

        ]

class CategorySerializer(serializers.ModelSerializer):
    collection_name = serializers.CharField(source='collection.name', read_only=True)
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "collection_name",
        ]