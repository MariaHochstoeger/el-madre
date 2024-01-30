from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic  # import generic django view
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# import Post, Comment and Category models from models.py
from .models import Post, Comment, Category
from .forms import CommentForm  # import CommentForm from forms.py

# VIEWS


# Class-based views
class PostList(generic.ListView):
    """
    Display a list of published :model:`blog.Post` entries
    and displays them as three posts per page.

    **Context**

    ``queryset``
        A list of :model:`blog.Post` instances.
    ``paginate_by``
        Number of posts per page

    **Template:**

    :template:`blog/index.html`
    """
    # returns all records from the Post model with status 1, ie published
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 3


class CatListView(ListView):
    """
    Display a list of published :model:`blog.Post` entries
    belonging to a specific category.

    **Context**

    ``catlist``
        A dictionary with keys 'cat' for the category name
        and 'posts' for a list of :model:`blog.Post` instances.

    **Template:**

    :template:`blog/category.html`
    """
    template_name = 'blog/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': (
             Post.objects
             .filter(category__name=self.kwargs['category'])
             .filter(status=1)
            )
        }
        return content


# Function-based views
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``favourite_status``
        A boolean indicating whether the current user has favorited the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    # Check if the post is a favorite for the current user
    favourite_status = False
    if request.user.is_authenticated:
        favourite_status = post.favourites.filter(id=request.user.id).exists()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for your comment!'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
            "favourite_status": favourite_status,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`.
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = True
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request,
                                 messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request,
                             messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def category_list(request):
    """
    Retrieve a list of categories excluding the default one.

    **Context**

    ``category_list``
        A list of :model:`blog.Category` instances.

    **Template:**

    :template:`blog/category.html`
    """
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context


def favourite_add(request, id):
    """
    Add or remove a post from the user's favorites.

    **Context**

    ``favourite_status``
        A boolean indicating whether the post is in the user's favorites.
    """
    post = get_object_or_404(Post, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
        favourite_status = False
        messages.add_message(request,
                             messages.SUCCESS, 'Removed from your favourites!')
    else:
        post.favourites.add(request.user)
        favourite_status = True
        messages.add_message(request,
                             messages.SUCCESS, 'Added to your favourites!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def favourite_list(request):
    """
    Display a list of the user's favorite posts.

    **Context**

    ``new``
        A queryset of :model:`blog.Post` instances that the user has favorited.

    **Template:**

    :template:`blog/favourites.html`
    """
    new = Post.objects.filter(favourites=request.user)
    return render(request, 'blog/favourites.html', {'new': new})
