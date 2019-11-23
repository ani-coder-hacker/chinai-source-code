from django.shortcuts import render

# Create your views here.
def post_list(request):
    args = {}
    return render(request, 'blog/post_list.html', args)

def home(request):
    args = {}
    return render(request, 'blog/home.html', args)
