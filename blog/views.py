from django.shortcuts import render,get_object_or_404
from .models import Post, Message

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    message = Message.objects.all()
    args = {
    'posts':posts,
    'message':message
    }
    return render(request, 'blog/post_list.html', args)

def home(request):
    message = Message.objects.all()
    posts = Post.objects.all().order_by('-published_date')[0:4]
    number_of_posts = Post.objects.all().count()
    args = {
    'message' : message,
    'posts' : posts,
    'number_of_posts': number_of_posts,
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
