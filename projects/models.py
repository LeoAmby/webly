from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length = 30)
    image = models.ImageField(uploads_to = 'images')
    description = models.TextField()
