from django.urls import path
from . import views

urlpatterns = [
    # Task 0: Index
    path('', views.index, name='index'),

    # Task 3: Blog post CRUD
    path('posts/', views.PostListView.as_view(), name='post_list'),  # List all posts
    path('posts/new/', views.PostCreateView.as_view(), name='post_create'),  # Create new post
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # View post details
    path('posts/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),  # Edit post
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete post
]