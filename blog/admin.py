from django.contrib import admin
from .models import Comment
from .models import Post

# Register Posts and Comments on the admin page
admin.site.register(Comment)
admin.site.register(Post)