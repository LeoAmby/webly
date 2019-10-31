
from django.urls import path, include, register_converter
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from sites.views import (
ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView)

urlpatterns = [
    path('', views.index, name="index"),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update', views.ProjectUpdateView, name='project-update'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='project-delete'),
    path('profile', views.profile, name="profile"),
    path('account', include("django.contrib.auth.urls")),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
