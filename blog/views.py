from django.shortcuts import render
from . models import blog,catagory,News,blogviews
# Create your views here.
def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def Blog(request,slug=None,blogid=None):
    if slug is not None:
        if blogid is None:
            allBlogs= blog.objects.filter(type=list(filter( lambda x:x[1]==slug, blog.Getchoices() ))[0][0])
            responce={
                'title':slug,
                slug: 'active',
                'blogs':allBlogs,
            }
            return render(request,'blog/blog.html',responce)
        else:
            Blogs= blog.objects.get(slug = blogid)
            ip = visitor_ip_address(request)
            viewob = blogviews.objects.filter(blogid=Blogs.id,ip = ip)
            if viewob.exists() == False:
                blogviews(blogid=Blogs,ip=ip).save()
            allBlogs= blog.objects.filter(type=list(filter( lambda x:x[1]==slug, blog.Getchoices() ))[0][0])
            responce= {
            'title': Blogs.blog_title,
            'blog':Blogs ,
            'ne': 'active',
            'blogs':allBlogs.filter(blog_catagory=Blogs.blog_catagory.id)
            }
            current = responce['blogs'].filter(id__lt = responce['blog'].id).count()
            responce['nextblog'] = responce['blogs'][current+1] if len(responce['blogs'])-1 > current else False
            responce['prevblog'] = responce['blogs'][current-1] if current > 0 else False
            responce['type'] = slug
            return render(request,'blog/post1.html',responce)
    # Blogs= blog.objects.get(slug= slug)
    # Blogss= blog.objects.all()[:3]
    # responce= {
    #     'title': Blogs.blog_title,
    #     'bl':'active',
    #    'blog':Blogs ,
    #    'blogs':Blogss 
    # }
def news(request, num=0):
    if num == 0:
        NEWS = News.objects.all()

        responce={
            'title':'News',
            'news': 'active',
            'blogs':NEWS
        }
        return render(request,'blog/news1.html',responce)
    Blogs= News.objects.get(id= num)
    Blogss= blog.objects.all()[:3]
    responce= {
        'title': Blogs.blog_title,
       'blog':Blogs ,
       'ne': 'active',
       'blogs':Blogss 
    }
    return render(request,'blog/post.html',responce)
    