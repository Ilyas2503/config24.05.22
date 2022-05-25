from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'post'

    def __str__(self):
        return self.title
# Create your models here.
