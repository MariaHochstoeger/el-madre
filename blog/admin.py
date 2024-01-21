from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin # extra functionality for posts written by superuser


@admin.register(Post) # decorator to register the class Post
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Registering models so that they appear on the admin site
admin.site.register(Comment)