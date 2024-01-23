from . import views # import views file
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'), # blank space '' signifies home page
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]