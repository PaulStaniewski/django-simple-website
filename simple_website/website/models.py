from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Gallery(models.Model):  # gallery model
    class Meta:  # meta
        verbose_name_plural = 'Galleries'  # verbose name
    title = models.CharField(max_length=150)  # title
    describe = models.CharField(max_length=100)  # describe
    image = models.ImageField()  # image field

    def __str__(self):
        return self.title  # return title


class Gallery360(models.Model):  # gallery360 model
    class Meta:  # meta
        verbose_name_plural = '360Galleries'  # verbose name
    image = models.ImageField(upload_to='')  # image
    title = models.CharField(max_length=80)  # title
    summary = models.CharField(max_length=100)  # summary

    def __str__(self):
        return self.title


STATUS = (  # status
    (0, "Draft"),  # draft
    (1, "Publish")  # publish
)


class Post(models.Model):  # post model
    title = models.CharField(max_length=200, unique=True)  # title
    slug = models.SlugField(max_length=200, unique=True)    # slug
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # author
    updated_on = models.DateTimeField(auto_now=True)  # updated on
    content = models.TextField()  # content
    created_on = models.DateTimeField(auto_now_add=True)  # created on
    status = models.IntegerField(choices=STATUS, default=0)  # status

    class Meta:  # meta
        ordering = ['-created_on']  # ordering

    def __str__(self):
        return self.title  # return title
