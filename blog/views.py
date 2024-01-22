from django.shortcuts import render, get_object_or_404
from django.views import generic # import generic django view
from .models import Post # import Post model

# VIEWS

# Class-based views
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1) # returns all records from the Post model with status 1, ie published
    template_name = "blog/index.html"
    paginate_by = 3


# Function-based views
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )