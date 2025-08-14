from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Post


# View to create a post, requiring 'can_create' permission
@permission_required("accounts.can_create", raise_exception=True)
def create_post(request):
    if request.method == "POST":
        # Create post logic here
        pass
    return render(request, "create_post.html")


# View to edit a post, requiring 'can_edit' permission
@permission_required("accounts.can_edit", raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        # Edit post logic here
        pass
    return render(request, "edit_post.html", {"post": post})


# View to delete a post, requiring 'can_delete' permission
@permission_required("accounts.can_delete", raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        # Delete post logic here
        post.delete()
    return render(request, "delete_post.html", {"post": post})
