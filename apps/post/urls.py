
from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.post.serializers import LikedPostSerializer
from .views import LikePostsView, PostViewSet, CommentCreateDeleteView, TagViewSet


router = DefaultRouter()
router.register('post', PostViewSet, 'post')
router.register('comment', CommentCreateDeleteView, 'comment')
router.register('tags', TagViewSet, 'tags')
urlpatterns = [
    path('liked/', LikePostsView.as_view(), name='liked')
]


urlpatterns += router.urls