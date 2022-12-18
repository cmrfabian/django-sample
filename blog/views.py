from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

from .models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Listing Page
def index(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'posts': posts })

# Create Post
def add(request):
    template = loader.get_template('create.html')
    return HttpResponse(template.render({}, request))

# Store Blog
def addrecord(request):
    x = request.POST['title']
    y = request.POST['description']
    post = Post(title=x, description=y)
    post.save()
    return HttpResponseRedirect(reverse('index'))

# Delete Post
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

# Update Post
def update(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))

# Update Post
def updaterecord(request, id):
    title = request.POST['title']
    description = request.POST['description']
    post = Post.objects.get(id=id)
    post.title = title
    post.description = description
    post.save()
    return HttpResponseRedirect(reverse('index'))

# Show Post
def show(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('show.html')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))

# Upload Image
def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'upload.html', {'file_url': file_url})
    return render(request, 'upload.html')