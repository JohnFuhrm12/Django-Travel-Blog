from django.shortcuts import render
from .models import Comment
from .models import CommentForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def start(request):
    return render(request, 'start.html')

def destinations(request):
    return render(request, 'destinations.html')

def sanandres(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            comment = form.cleaned_data.get('comment')
            form = CommentForm()
    else:
        form = CommentForm()
    context = {
        'comments': Comment.objects.all(),
        'form': form
    }
    return render(request, 'sanandres.html', context)
