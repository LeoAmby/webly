from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 30)
    photo = models.ImageField(upload_to = 'images')
    description = models.TextField()
    link = models.URLField(max_length = 200)

    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, default='', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'images')
    bio = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return f'{self.user.username} Profile'