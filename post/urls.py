from django.urls import path
from .views import PostCreateView, CommentCreateView, CommentUpdateView, CommentDeleteView,PostListView

urlpatterns = [
    path('posts/',PostListView.as_view(),name='post-list'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]