from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    byline = models.CharField(max_length=200)
    content = models.TextField()
    batch = models.IntegerField()
    display = models.BooleanField(default=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
