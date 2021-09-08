from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('<slug:slug>/', views.Blog, name = 'blog'), 
    path('<slug:slug>/<slug:blogid>', views.Blog, name = 'blog'), 
]