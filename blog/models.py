from email.mime import image
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    description = models.TextField()
    last_modified = models.DateTimeField(auto_created=True, auto_now=True)
    published_on = models.DateTimeField(auto_now_add=True)
