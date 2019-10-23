from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'images')
    description = models.TextField()


class Profile(models.Model):
    photo = models.ImageField(upload_to = 'images')
    bio = models.TextField()
    projects = models.ForeignKey(Projects)
    email = models.EmailField()
