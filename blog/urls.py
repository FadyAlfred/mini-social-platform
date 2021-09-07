from django.urls import path, include

from rest_framework.routers import DefaultRouter

from blog.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
# router.register(r'comments', CommentViewSet, basename='comments')
# router.register(r'likes', LikeViewSet, basename='likes')

urlpatterns = [
    path('', include(router.urls)),
]