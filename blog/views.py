from django.shortcuts import render
from django.views import generic # import generic django view
from .models import Post # import Post model

# VIEWS
# CLASS-BASED VIEWS
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) # returns all records from the Post model with status 1, ie published
    template_name = "post_list.html" # post_list: post refers to the model, list to the generic view