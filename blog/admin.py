from django.contrib import admin
from . models import blog,catagory,News,blogviews
# Register your models here.
admin.site.register(catagory)
admin.site.register(blog)
admin.site.register(News)
admin.site.register(blogviews)