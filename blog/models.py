from django.db import models
from ckeditor.fields import RichTextField
from ourwork.models import get_random_string,unique_slug_generator
import datetime
# Create your models here.
class catagory(models.Model):
    catagory = models.CharField(max_length=50)
    def __str__(self):
        return self.catagory
class  blog(models.Model):
	def Getchoices():
		return (('1','blog'),('2','news'))
	blog_title = models.CharField(max_length=50)
	blog_content = RichTextField()
	blog_time = models.DateTimeField(auto_now=True)
	blog_share = models.IntegerField(default=0)
	blog_views = models.IntegerField(default=0)
	blog_owner = models.CharField(max_length=50)
	blog_image = models.ImageField(upload_to = 'wesiteblog/images', default= "")
	blog_catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
	type = models.CharField(max_length=1,choices=Getchoices())
	slug = models.SlugField(blank=True)
	def __str__(self):
		return self.blog_owner
	def save(self, *args, **kwargs):
		self.slug = unique_slug_generator(blog,self.blog_title)
		super(blog, self).save(*args, **kwargs)
class  News(models.Model):
	blog_title = models.CharField(max_length=50)
	blog_content = RichTextField()
	blog_time = models.DateTimeField(auto_now=True)
	blog_share = models.IntegerField(default=0)
	blog_views = models.IntegerField(default=0)
	blog_owners = models.CharField(max_length=50)
	blog_image = models.ImageField(upload_to = 'wesiteblog/images', default= "")
	blog_catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
	def __str__(self):
		return self.blog_owners