from django.shortcuts import render
from .models import Comment
from .models import CommentForm
from .models import CommentRiviera
from .models import CommentFormRiviera
from .models import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'johnfuhrmeister12@gmail.com', ['johnfuhrmeister12@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    form = ContactForm()
    return render(request, 'about.html', {'form': form})

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