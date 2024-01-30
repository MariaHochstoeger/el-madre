from django.contrib import admin
# extra functionality for posts written by superuser
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Category


# Registering models so that they appear on the admin site
@admin.register(Post)  # decorator to register the class Post
class PostAdmin(SummernoteModelAdmin):
    """Admin configuration for the Post model.

    This class extends the SummernoteModelAdmin to enhance the post creation
    experience for superusers.
    It provides a rich text editor for the post content.

    Attributes:
        list_display (tuple): Fields to display in the list view of posts.
        search_fields (list):
        Fields to search for when using the admin search bar.
        list_filter (tuple): Fields to filter posts by in the admin list view.
        prepopulated_fields (dict):
        Automatically populate the slug field based on the title.
        summernote_fields (tuple): Fields to enable the Summernote editor for.
        actions (list): Custom admin actions, in this case, 'make_published'.

    Methods:
        make_published: Admin action to mark selected posts as published.

    Short Description:
        Mark selected posts as published in bulk.
    """
    # added 'author' for better UX
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    search_fields = ['title', 'content']
    # added 'author' for better UX
    list_filter = ('status', 'created_on', 'author')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

    # Publish several posts at once
    actions = ['make_published']

    def make_published(self, request, queryset):
        """Mark selected posts as published.

        This admin action updates the status of selected posts to 'Published'.

        Parameters:
            request (HttpRequest): The request object.
            queryset (QuerySet): The selected posts.

        Returns:
            None
        """
        queryset.update(status=1)
    make_published.short_description = "Mark selected posts as published"


# Register Comment and Category models
admin.site.register(Comment)


admin.site.register(Category)
