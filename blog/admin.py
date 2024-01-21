from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin # extra functionality for posts written by superuser


@admin.register(Post) # decorator to register the class Post
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'status', 'created_on') # added 'author' for better UX
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'author') # added 'author' for better UX
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    # Custom code: publish several posts at once
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(status=1)
    make_published.short_description = "Mark selected posts as published"

# Registering models so that they appear on the admin site
admin.site.register(Comment)