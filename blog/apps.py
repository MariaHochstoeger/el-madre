from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Django application configuration class for the 'blog' app.

    This class defines the configuration settings for the 'blog' app, including the
    default primary key type for models in the app.

    Attributes:
        default_auto_field (str): The default primary key type for models in the app.
        name (str): The name of the app.

    Short Description:
        Configuration settings for the 'blog' app in a Django project.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
