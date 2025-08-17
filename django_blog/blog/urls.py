from django.urls import path
from . import views

urlpatterns = [
    # Task 0: Index
    path('', views.index, name='index'),

    # Task 3: Blog post CRUD (singular 'post/')
    path('post/', views.PostListView.as_view(), name='post_list'),  # List all posts
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),  # Create new post
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # View post details
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),  # Edit post
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),  # Delete post
]