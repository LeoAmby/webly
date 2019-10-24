from django.shortcuts import render
from .models import Project, Profile
from django.http import HttpResponse


def index(request):
    project = Project.objects.all()
    params = {
        'project':project,
        
    }
    return render (request, 'index.html', params)
    