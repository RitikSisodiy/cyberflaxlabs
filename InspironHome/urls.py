"""InspironHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from api import views as apiviews
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

#creating router object
router = DefaultRouter()
router.register('ourworkcat',apiviews.ourWork_catModelViewset,basename='ourwork')
router.register('ourcatbanner',apiviews.headbannerModelViewset,basename='headbanner')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name ='home'),
    path('', views.index, name ='home'),
    path('about/', views.about, name ='about'),
    path('blog/', include('blog.urls')),
    path('service/', include('service.urls')),
    path('ourwork/', include('ourwork.urls')),
    path('contact/', include('contact.urls')),
    path('api/',include(router.urls ))
    
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
