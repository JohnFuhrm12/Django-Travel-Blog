from django import forms
from django.db import models
from django.forms import ModelForm
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse, reverse_lazy

# Blog Post Database info
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    # Slugify (text-text-text) Title for URL
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    # When creating a new post return you to the same page
    def get_absolute_url(self):
        return reverse_lazy('posts')

    # About Me Page Email Contact Form
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)

# Database fields for comment info
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)
    reply = models.ForeignKey('Comment', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    # Order comments by most recent
    class Meta:
        ordering = ["-id"]

    # Make it appear nice on admin page
    def __str__(self):
        return '%s - %s'% (self.post.title, self.name)

# Link comment database model to a form model
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment', 'post']
        widgets = {'post': forms.HiddenInput()}