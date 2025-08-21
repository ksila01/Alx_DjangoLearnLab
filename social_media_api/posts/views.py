from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("author").all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at", "updated_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=["get", "post"])
    def comments(self, request, pk=None):
        post = self.get_object()
        if request.method == "GET":
            qs = post.comments.select_related("author").all()
            page = self.paginate_queryset(qs)
            ser = CommentSerializer(page, many=True)
            return self.get_paginated_response(ser.data)
        # POST (create)
        ser = CommentSerializer(data=request.data, context={"request": request})
        ser.is_valid(raise_exception=True)
        ser.save(post=post, author=request.user)
        comment = Comment.objects.get(pk=ser.data["id"])
        # Notify post author about new comment
        create_notification(recipient=comment.post.author, actor=request.user, verb="commented", target=comment.post)
        return Response(ser.data, status=status.HTTP_201_CREATED)
    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            # Notify the post author
            create_notification(recipient=post.author, actor=request.user, verb="liked", target=post)
            return Response({"detail": "Liked."}, status=201)
        return Response({"detail": "Already liked."}, status=200)

    @action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        post = self.get_object()
        deleted, _ = Like.objects.filter(post=post, user=request.user).delete()
        if deleted:
            return Response({"detail": "Unliked."}, status=200)
        return Response({"detail": "You had not liked this post."}, status=400)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related("author", "post").all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    search_fields = ["content"]
    ordering_fields = ["created_at", "updated_at"]

    def get_queryset(self):
        qs = super().get_queryset()
        post_id = self.request.query_params.get("post")
        if post_id:
            qs = qs.filter(post_id=post_id)
        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_ids = user.following.values_list("id", flat=True)
        return Post.objects.filter(author_id__in=following_ids).select_related("author").order_by("-created_at")
