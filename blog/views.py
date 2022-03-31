from django.shortcuts import render
from .models import Comment
from .models import CommentForm
from .models import CommentRiviera
from .models import CommentFormRiviera

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

def rivieramaya(request):
    if request.method == 'POST':
        form = CommentFormRiviera(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            comment = form.cleaned_data.get('comment')
            form = CommentFormRiviera()
    else:
        form = CommentFormRiviera()
    context = {
        'comments': CommentRiviera.objects.all(),
        'form': form
    }
    return render(request, 'rivieramaya.html', context)