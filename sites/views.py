from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,  CreateView, UpdateView, DeleteView
from .models import Project, Profile
from django.http import HttpResponse
from register.forms import ProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 



def index(request):
    projects =Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html', context)
    

def profile(request):
    return render(request, 'profile.html')


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



def ProjectUpdateView(request, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect ('/')
    else:
        form = ProjectForm()
    context = {
        'form':form,
    }
    return render(request, 'sites/project_form.html', context)

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def test_func(self):
    #     project = self.get_object()
    #     if self.request.user == project.author:
    #         return True
    #     return False

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'
    
    def test_func(self):
        project = self.get_object()
        if self.request.user == project.author:
            return True
        return False