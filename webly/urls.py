"""webly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, register_converter
from sites import views
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth import views
from register import views as auth_views
from sites.views import (
ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectListView.as_view(), name='index'),
    path('', views.index, name="index"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='project-update'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project-delete'),
    path('register/', auth_views.register, name="register"),
    path('profile', auth_views.profile, name="profile"),
    path('', include("django.contrib.auth.urls")),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
