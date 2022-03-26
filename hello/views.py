from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def start(request):
    return render(request, 'start.html')

def destinations(request):
    return render(request, 'destinations.html')

def test(request):
    context = {
      'posts': Post.objects.all()
    }
    return render(request, 'testpage.html', context)