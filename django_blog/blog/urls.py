from django.urls import path
from . import views
from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


urlpatterns = [
    # Task 0: Index
    path('', views.index, name='index'),

    # Task 3: Blog post CRUD (singular 'post/')
    path('post/', views.PostListView.as_view(), name='post_list'),  # List all posts
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Create new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # View post details
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),  # Edit post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete post

    # Task 4: Comment URLs
    path('post/<int:post_id>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]