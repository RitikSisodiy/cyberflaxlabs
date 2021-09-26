from ourwork.models import unique_slug_generator
from django.db import models

# Create your models here.
class service(models.Model):
    icon = models.ImageField(upload_to = 'media/ourwork',default= '')
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(service,self.title)
        super(service, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class ServiceSubMenu(models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE,related_name="ServiceSubMenu")
    Submenu = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(ServiceSubMenu,self.Submenu)
        super(ServiceSubMenu, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.Submenu)
    

class subservices(models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    sub_service = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=500)
    tag_content = models.CharField(max_length=5000)
    Optionalicon = models.FileField(upload_to = 'media/subservice',blank=True)
    def __str__(self):
        return str(self.sub_service)

class expertise(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    Select_type = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    expertise = models.CharField(max_length=500 ,blank=True)
    def __str__(self):
        return str(self.Select_type)
class sub_expertise(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=500)
class sub_expertise_icon(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    icon = models.FileField(upload_to = 'media/subexpertise',default= '')
    title = models.CharField(max_length=500,blank=True)
    def __str__(self):
        return str(self.subservices )
class subproject(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    project_type = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    img = models.ImageField(upload_to = 'media/subproject',default= '')
    name = models.CharField(max_length=50)

class headbanner(models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    sub_service = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    banner =  models.ImageField(upload_to = 'media/subservice',default= '')
    banner_icon =  models.ImageField(upload_to = 'media/subservice',default= '')
    banner_title = models.CharField(max_length=100)
    banner_content = models.CharField(max_length=500)
    def __str__(self):
        return str(self.sub_service)

class WhatWeDo(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    icon = models.FileField(upload_to = 'media/whatwedo',default= '')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    def __str__(self):
        return str(self.subservices)
class serviceFact(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    icon = models.FileField(upload_to = 'media/fact',default= '')
    content = models.CharField(max_length=500)
    
class sub_benifit(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    icon = models.FileField(upload_to = 'media/fact',default= '')
    content = models.CharField(max_length=500)
    def __str__(self):
        return str(self.subservices)
class sub_serviceWeOffer(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    icon = models.FileField(upload_to = 'media/serviceoffer',default= '')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    def __str__(self):
        return str(self.subservices)
class devLifecycle(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    icon = models.FileField(upload_to = 'media/fact',default= '')
    def __str__(self):
        return str(self.subservices)
class engagement(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000)
    icon = models.FileField(upload_to = 'media/fact',default= '')
    def __str__(self):
        return str(self.subservices)
class expertiseWithTitleIcon(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    icon = models.FileField(upload_to = 'media/expertise',default= '' )
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=5000,blank= True)
    def __str__(self):
        return str(self.subservices)
class middleimage(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    img =  models.ImageField(upload_to = 'media/middle',default= '')
    def __str__(self):
        return str(self.subservices)
class bottomdiv(models.Model):
    services =  models.ForeignKey(service, on_delete=models.CASCADE,default=1)
    subservices = models.ForeignKey(ServiceSubMenu, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    img =  models.ImageField(upload_to = 'media/middle',default= '')
    content = models.CharField(max_length=5000)