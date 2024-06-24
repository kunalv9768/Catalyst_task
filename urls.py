from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('', include('main.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_file, name='upload'),
    path('query/', views.query_builder, name='query_builder'),
    path('users/', views.user_list, name='user_list'),
]
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def upload_file(request):
    return render(request, 'upload.html')

def query_builder(request):
    return render(request, 'query_builder.html')

def user_list(request):
    return render(request, 'users.html')
