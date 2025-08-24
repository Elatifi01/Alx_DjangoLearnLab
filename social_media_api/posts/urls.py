from rest_framework.routers import DefaultRouter
from django.urls import include
from .views import PostViewSet, CommentViewSet
from django.urls import path
from .views import LikePostView, UnlikePostView, FeedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
    path('feed/', FeedView.as_view(), name='feed'),
]
