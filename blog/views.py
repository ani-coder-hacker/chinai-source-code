from django.shortcuts import render,get_object_or_404
from .models import Post, Message
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def post_list(request):
    posts_list = Post.objects.all().order_by('-published_date')
    paginator = Paginator(posts_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    message = Message.objects.all().order_by('-id')
    args = {
    'posts':posts,
    'messages':message
    }
    return render(request, 'blog/post_list.html', args)

def search(request):
    posts = Post.objects.all().order_by('-published_date')
    query = request.GET.get("q")
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(content__icontains=query) |
            Q(batch__icontains=query)
            ).distinct()
    message = Message.objects.all().order_by('-id')
    args = {
    'posts':posts,
    'messages':message
    }
    return render(request, 'blog/search.html', args)

def home(request):
    message = Message.objects.all().order_by('-id')
    x = Posts.objects.all()
    if x:
        firstpost = Post.objects.all().order_by('-published_date')[0]
        posts = Post.objects.all().order_by('-published_date')[1:4]
    else:
        posts = []
        firstpost = []
    args = {
    'messages' : message,
    'firstpost' : firstpost,
    'posts' : posts,
    }
    return render(request, 'blog/home.html', args)

def cat_dr(request):
    posts = Post.objects.filter(category='DR')
    message = Message.objects.all().order_by('-id')
    heading = 'Descriptions'
    args = {
    'posts' : posts,
    'heading' : heading,
    'messages' : message
    }
    return render(request, 'blog/cat.html', args)

def cat_na(request):
    posts = Post.objects.filter(category='NA')
    message = Message.objects.all().order_by('-id')
    heading = 'Nature'
    args = {
    'posts' : posts,
    'heading' : heading,
    'messages' : message
    }
    return render(request, 'blog/cat.html', args)

def cat_th(request):
    posts = Post.objects.filter(category='TH')
    message = Message.objects.all().order_by('-id')
    heading = 'Threshold'
    args = {
    'posts' : posts,
    'heading' : heading,
    'messages' : message
    }
    return render(request, 'blog/cat.html', args)

def cat_pe(request):
    posts = Post.objects.filter(category='E')
    message = Message.objects.all().order_by('-id')
    heading = 'Experiences'
    args = {
    'posts' : posts,
    'heading' : heading,
    'messages' : message
    }
    return render(request, 'blog/cat.html', args)

def cat_sc(request):
    posts = Post.objects.filter(category='SC')
    message = Message.objects.all().order_by('-id')
    heading = 'School'
    args = {
    'posts' : posts,
    'heading' : heading,
    'messages' : message
    }
    return render(request, 'blog/cat.html', args)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    message = Message.objects.all().order_by('-id')
    args = {
        'post' : post,
        'messages' : message,
    }
    return render(request, 'blog/post_detail.html',args)

def about(request):
    message = Message.objects.all().order_by('-id')
    args = {
     'messages' : message,
    }
    return render(request, 'blog/about.html', args)

def cat(request):
    message = Message.objects.all().order_by('-id')
    args = {
     'messages' : message,
    }
    return render(request, 'blog/categories.html', args)

def contribute(request):
    message = Message.objects.all().order_by('-id')
    args = {
     'messages' : message,
    }
    return render(request, 'blog/contribute.html', args)
