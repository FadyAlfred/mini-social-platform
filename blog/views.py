from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, mixins, filters, decorators, parsers, response, status
from rest_framework.views import Response

from blog.models import Post, Comment, Like
from blog.serializers import PostSerializer, PostDetailSerializer, PostAttachmentSerializer, CommentSerializer, \
    LikeSerializer
from blog.permissions import IsOwner


class PostViewSet(viewsets.ViewSet, mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']

    def list(self, request):
        serializer = PostSerializer(self.get_queryset(), many=True)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)

    @decorators.action(
        detail=True,
        methods=['PUT'],
        parser_classes=[parsers.MultiPartParser],
        permission_classes=(IsOwner,)
    )
    def attachment(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostAttachmentSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)

    @decorators.action(detail=True, methods=['GET'])
    def detail(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

    @decorators.action(detail=True, methods=['GET', 'POST'])
    def like(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'GET':
            queryset = Like.objects.filter(post=post)
            serializer = LikeSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            current_user_post_like = Like.objects.filter(user=self.request.user, post=post)
            if current_user_post_like:
                return Response({"message": "Multiple likes not allowed"}, status=400)

            serializer = LikeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user, post=post)
            return Response(serializer.data, status.HTTP_201_CREATED)

    @decorators.action(detail=True, methods=['GET', 'POST'])
    def comment(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == 'GET':
            queryset = Comment.objects.filter(post=post)
            serializer = CommentSerializer(queryset, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=self.request.user, post=post)
            return Response(serializer.data, status.HTTP_201_CREATED)
