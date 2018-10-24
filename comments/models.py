from django.db import models
from django.contrib.auth.models import User
from posts.models import Posts


# Create your models here.
class Comments(models.Model):

    author  = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    post    = models.ForeignKey(Posts, on_delete=models.CASCADE)
    content = models.TextField(max_length=512)
    date    = models.DateTimeField(auto_now_add=True)
    score   = models.IntegerField(default=0)



    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.content