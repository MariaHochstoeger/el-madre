from . import views # import views file
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
]