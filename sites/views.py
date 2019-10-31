from django.shortcuts import render
from django.views.generic import ListView, DetailView,  CreateView, UpdateView, DeleteView
from .models import Project, Profile
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 



def index(request):
    # context = {
    #     'projects': Project.objects.all()
    # }
   
    # project = Project.objects.all()
    # params = {
    #     'project':project,
        
    # }
    print('hbhedfhkdjhuhsufhrkjh')
    projects =Project.objects.all()
    print(projects)
    return render (request, 'index.html', {'projects':projects})
    

class ProjectListView(ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'project'
    # projects =Project.objects.all()
    ordering = ['-date_posted']

class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'photo', 'description', 'link']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'photo', 'description', 'link']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'
    
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False