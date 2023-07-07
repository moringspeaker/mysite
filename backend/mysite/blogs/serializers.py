from rest_framework import serializers
from .models import Blog


class BlogsSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
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
            "category_name",
        ]

    def get_category_name(self, obj):
        return obj.category.name
