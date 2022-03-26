from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, 'index.html')

def page(request):
    return render(request, 'page.html')

def test(request):
    context = {
      'posts': Post.objects.all()
    }
    return render(request, 'testpage.html', context)