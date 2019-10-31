from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Project, Profile
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin



def index(request):
    context = {
        'projects': Project.objects.all()
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


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'photo', 'description', 'link']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)