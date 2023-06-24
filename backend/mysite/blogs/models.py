
# Create your models here.
from django.db import models
from django.utils import timezone, dateformat

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name

class Collection(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.AutoField(primary_key=True)

    ENtitle = models.CharField(max_length=200,blank=True)
    ENcontent = models.TextField()
    ENauthor = models.CharField(max_length=200,default='ChenYu')
    ENsummary = models.CharField(max_length=200,default='The weak is the recognition of love, just as giving up is the antidote of noise')

    CHtitle = models.CharField(max_length=200,blank=True)
    CHcontent = models.TextField()
    CHauthor = models.CharField(max_length=200,default='尘语')
    CHsummary = models.CharField(max_length=200,default='惟柔弱是爱愿的识别，正如放弃是喧嚣的解剂')

    cover = models.ImageField(upload_to='medias/covers/', default='static/no-img.jpg')
    created_date = models.DateTimeField(default=timezone.now)

    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    def __str__(self):
        # return f"Blog: {self.ENtitle or self.CHtitle} - Category: {self.category.name}"
        return self.ENtitle or self.CHtitle
    def formatted_created_date(self):
        return self.created_date.strftime("%Y-%m-%d %H:%M:%S")
    def save(self, *args, **kwargs):
        if self.collection:
            self.category = self.collection.category
        super().save(*args, **kwargs)
