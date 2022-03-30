from django.db import models
from django.forms import ModelForm

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