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
    message = Message.objects.all()
    args = {
    'posts':posts,
    'message':message
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
    message = Message.objects.all()
    args = {
    'posts':posts,
    'message':message
    }
    return render(request, 'blog/search.html', args)

def home(request):
    message = Message.objects.all()
    firstpost = Post.objects.all().order_by('-published_date')[0]
    posts = Post.objects.all().order_by('-published_date')[1:4]
    args = {
    'message' : message,
    'firstpost' : firstpost,
    'posts' : posts,
    }
    return render(request, 'blog/home.html', args)

def cat_dr(request):
    posts = Post.objects.filter(category='DR')
    message = Message.objects.all()
    heading = 'Descriptions'
    args = {
    'posts' : posts,
    'heading' : heading,
    'message' : message
    }
    return render(request, 'blog/cat.html', args)

def cat_na(request):
    posts = Post.objects.filter(category='NA')
    message = Message.objects.all()
    heading = 'Nature'
    args = {
    'posts' : posts,
    'heading' : heading,
    'message' : message
    }
    return render(request, 'blog/cat.html', args)

def cat_th(request):
    posts = Post.objects.filter(category='TH')
    message = Message.objects.all()
    heading = 'Threshold'
    args = {
    'posts' : posts,
    'heading' : heading,
    'message' : message
    }
    return render(request, 'blog/cat.html', args)

def cat_pe(request):
    posts = Post.objects.filter(category='E')
    message = Message.objects.all()
    heading = 'Experiences'
    args = {
    'posts' : posts,
    'heading' : heading,
    'message' : message
    }
    return render(request, 'blog/cat.html', args)

def cat_sc(request):
    posts = Post.objects.filter(category='SC')
    message = Message.objects.all()
    heading = 'School'
    args = {
    'posts' : posts,
    'heading' : heading,
    'message' : message
    }
    return render(request, 'blog/cat.html', args)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    args = {}
    return render(request, 'blog/about.html', args)

def cat(request):
    args = {}
    return render(request, 'blog/categories.html', args)

def contribute(request):
    args = {}
    return render(request, 'blog/contribute.html', args)
