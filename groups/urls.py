from django.urls import path
from .views import (
    CreateGroupView, GroupMemberListView, GroupPostListView, UserJoinGroupView, UserLeaveGroupView, CreateAdminView, RemoveAdminView,
    CreatePostView, RemovePostView, EditPostView, EditGroupView,
    AllGroupsView, PublicGroupsView, PrivateGroupsView
)

urlpatterns = [
    path('create/', CreateGroupView.as_view(), name='create_group'),
    path('<int:group_id>/join/', UserJoinGroupView.as_view(), name='user_join_group'),
    path('<int:group_id>/leave/', UserLeaveGroupView.as_view(), name='user_leave_group'),
    path('<int:group_id>/admins/', CreateAdminView.as_view(), name='create_admin'),
    path('<int:group_id>/admins/<int:pk>/', RemoveAdminView.as_view(), name='remove_admin'),
    path('<int:group_id>/posts/', CreatePostView.as_view(), name='create_post'),
    path('posts/<int:post_id>/', RemovePostView.as_view(), name='remove_post'),
    path('posts/<int:post_id>/edit/', EditPostView.as_view(), name='edit_post'),
    path('<int:group_id>/edit/', EditGroupView.as_view(), name='edit_group'),
    path('groups/', AllGroupsView.as_view(), name='all_groups'),
    path('public/', PublicGroupsView.as_view(), name='public_groups'),
    path('private/', PrivateGroupsView.as_view(), name='private_groups'),
    path('<int:group_id>/members/', GroupMemberListView.as_view(), name='group_members'),
    path('<int:group_id>/posts/', GroupPostListView.as_view(), name='group_posts'),
]
