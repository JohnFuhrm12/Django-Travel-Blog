"""djangowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

# Configure URLs
urlpatterns = [
    path('', views.index, name='home'),
    path('admin', admin.site.urls, name='admin'),
    path('about', views.about, name='about'),
    path('start', views.start, name='start'),
    path('destinations', views.destinations, name='destinations'),
    path('méxico', views.mexico, name='mexico'),
    path('colombia', views.colombia, name='colombia'),
    path('argentina', views.argentina, name='argentina'),
    path('posts', views.Posts.as_view(), name='posts'),
    path('posts/<slug:slug>', views.ArticleDetailView.as_view(), name='article-detail'),
    path('newpost', views.AddPost.as_view(), name='add-post'),
    path('test/editpost/<slug:slug>', views.EditPost.as_view(), name='edit-post'),
    path('test/deletepost/<slug:slug>', views.DeletePost.as_view(), name='delete-post'),
]

