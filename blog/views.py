from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def start(request):
    return render(request, 'start.html')

def destinations(request):
    return render(request, 'destinations.html')

def sanandres(request):
    return render(request, 'sanandres.html')
