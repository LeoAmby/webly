from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Project, Profile
from django.http import HttpResponse


def index(request):
    context = {
        'project': Project.objects.all()
    }
    # project = Project.objects.all()
    # params = {
    #     'project':project,
        
    # }
    return render (request, 'index.html', context)
    

class ProjectListView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'project'
    ordering = ['-date_posted']

class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project
    fields = ['title', 'photo', 'description', 'link']