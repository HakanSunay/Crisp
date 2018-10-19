from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'