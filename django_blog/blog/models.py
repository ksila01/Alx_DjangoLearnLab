from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# -----------------------------
# Task 3: Post Model
# -----------------------------
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')  # Task 4: Tagging

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})


# -----------------------------
# Task 4: Comment Model
# -----------------------------
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on "{self.post.title}"'


# -----------------------------
# Task 4: Tag Model
# -----------------------------
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('posts_by_tag', kwargs={'tag_name': self.name})
