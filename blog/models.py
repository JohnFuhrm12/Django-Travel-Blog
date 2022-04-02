from django.db import models
from django.forms import ModelForm
from django import forms

# About Me Page Email Contact Form
class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)

# Create database fields for comment info
class Comment(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.comment

# Link comment database model to a form model
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']


# Create database fields for comment info for each page
class CommentRiviera(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.comment

# Link comment database model to a form model
class CommentFormRiviera(ModelForm):
    class Meta:
        model = CommentRiviera
        fields = ['name', 'comment']

# Create database fields for comment info for each page
class CommentBuenosAires(models.Model):
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=150)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.comment

# Link comment database model to a form model
class CommentFormBuenosAires(ModelForm):
    class Meta:
        model = CommentBuenosAires
        fields = ['name', 'comment']