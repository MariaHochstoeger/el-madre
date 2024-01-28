from django.db import models
# import built-in User from Django
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# MODELS
class Category(models.Model):
    """
    Stores a single category related to :model:`blog.Post`.
    """
    name = models.CharField(max_length=50)

    # Change category identifier to a string literal
    def __str__(self):
        return f"{self.name}" 


# Status options for status variable
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Stores a single blog post entry related to :model:`auth.User` and to :model:`blog.Category`.
    """
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    # add a favourites field which will hold the IDs of all Users which favourited this post
    favourites = models.ManyToManyField(User, related_name='favourite', default=None, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    # make categories very difficult to delete, set default category to Miscellaneous (1)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)

    # Metadata within the model
    # Order posts by date created starting with the most recent
    class Meta:
        ordering = ["-created_on"]

    # Change post identifier to a string literal
    def __str__(self):
        return f"{self.title} | written by {self.author}" 


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`blog.Post`.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)

    # Metadata within the model
    # Order comments by date created starting with the most recent
    class Meta:
        ordering = ["-created_on"]

    # Change comment identifier to a string literal
    def __str__(self):
        shortened_date = self.created_on.strftime("%Y-%m-%d")  # Adjust the format of the date to only include year, month and day
        return f"Comment: '{self.body}' by {self.author} commented on {shortened_date}" # String literal is my own