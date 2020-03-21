from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    DESCRIPTIONS = 'DR'
    NATURE = 'NA'
    THRESHOLD = 'TH'
    EXP = 'E'
    SCHOOL = 'SC'

    CAT_CHOICES = [
    (DESCRIPTIONS, 'Descriptions'),
    (NATURE, 'Nature'),
    (THRESHOLD, 'Threshold'),
    (EXP, 'Experiences'),
    (SCHOOL, 'School')
    ]

    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=300, default="https://images.unsplash.com/photo-1584713284836-873df2d32409?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60")
    category = models.CharField(
    max_length=2,
    choices=CAT_CHOICES,
    default=SCHOOL
    )
    content = models.TextField()
    batch = models.IntegerField()
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    subject = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    def __str__(self):
        return self.subject
