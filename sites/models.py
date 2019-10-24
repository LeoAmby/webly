from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 30)
    photo = models.ImageField(upload_to = 'images')
    description = models.TextField()
    link = models.URLField(max_length = 200)

    def __str__ (self):
        return self.title


class Profile(models.Model):
    image = models.ImageField(upload_to = 'images')
    bio = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.bio