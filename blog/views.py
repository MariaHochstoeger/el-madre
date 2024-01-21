from django.shortcuts import render
from django.views import generic # import generic django view
from .models import Post # import Post model

# VIEWS
# CLASS-BASED VIEWS
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"