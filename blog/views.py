from django.shortcuts import render
from .models import Blog
# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html',({'blogs': blogs, 'blog_detail' : blog_detail}))


def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blog' : blog})


