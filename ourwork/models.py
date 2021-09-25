from django.db import models

from django.db import models
import random ,string
from django.utils.text import slugify

def get_random_string(size):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    slug=new_slug
    Klass = instance
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = slugify(str(slug)+get_random_string(4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slugify(slug)
    


# Create your models here.
class ourwork_cat(models.Model):
    title = models.CharField(max_length= 100)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = unique_slug_generator(ourwork_cat,self.title)
        super(ourwork_cat, self).save(*args, **kwargs)
class headbanner (models.Model):
    catagory = models.ForeignKey(ourwork_cat, on_delete=models.CASCADE,default=1,related_name="headbanner")
    title = models.CharField(max_length= 100)
    content = models.CharField(max_length= 5000)
    projecticon = models.ImageField(upload_to="ourwork/projecticon")
    projectimage = models.ImageField(upload_to="ourwork/projectimage")
    projectTitle = models.CharField(max_length= 200)
    projectsource = models.ImageField(upload_to="ourwork/projectsource")
    sourceLink= models.CharField(max_length= 500)
    projectlink= models.CharField(max_length= 500,blank = True)
    def __str__(self):
        return str(self.catagory)

class Work(models.Model):
    catagory = models.ForeignKey(ourwork_cat, on_delete=models.CASCADE,default=1)
    projectimage = models.FileField(upload_to="ourwork/projectimage" , blank = True)
    projecticon = models.FileField(upload_to="ourwork/projecticon",blank = True)
    projectTitle = models.CharField(max_length= 200,blank = True)
    content = models.CharField(max_length= 5000,blank = True)
    projectsource = models.FileField(upload_to="ourwork/projectsource",blank = True)
    sourceLink= models.CharField(max_length= 500,blank = True)
    projectsource1 = models.FileField(upload_to="ourwork/projectsource",blank = True)
    sourceLink1= models.CharField(max_length= 500,blank = True)
    projectlink= models.CharField(max_length= 500,blank = True)
    def __str__(self):
        return str(self.catagory)