from django.contrib import admin
from .models import Post, Comment

# Register your models here so that they appear on the admin site
admin.site.register(Post)
admin.site.register(Comment)