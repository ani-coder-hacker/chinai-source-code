from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    DESCRIPTIONS = 'DR'
    NATURE = 'NA'
    THRESHOLD = 'TH'
    PEREXP = 'PE'
    SCHOOL = 'SC'

    CAT_CHOICES = [
    (DESCRIPTIONS, 'Descriptions'),
    (NATURE, 'Nature'),
    (THRESHOLD, 'Threshold'),
    (PEREXP, 'Personal Experiences'),
    (SCHOOL, 'School')
    ]

    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    byline = models.CharField(max_length=200)
    category = models.CharField(
    max_length=2,
    choices=CAT_CHOICES,
    default=SCHOOL
    )
    content = models.TextField()
    batch = models.IntegerField()
    display = models.BooleanField(default=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    content = models.CharField(max_length=200, blank=True)
