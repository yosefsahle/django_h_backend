from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Group, GroupAdmin, GroupMember, GroupPost
from .serializer import (
    GroupSerializer, GroupAdminSerializer, GroupMemberSerializer, 
    GroupPostSerializer, GroupPostCreateSerializer
)
from rest_framework.exceptions import NotFound

#CREATE GROUP VIEW
class CreateGroupView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()



class UserJoinGroupView(generics.CreateAPIView):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        group_id = self.kwargs['group_id']
        group = Group.objects.get(id=group_id)
        serializer.save(user=user, group=group)

class UserLeaveGroupView(generics.DestroyAPIView):
    queryset = GroupMember.objects.all()
    serializer_class = GroupMemberSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        group_id = self.kwargs['group_id']
        try:
            return GroupMember.objects.get(user=user, group_id=group_id)
        except GroupMember.DoesNotExist:
            raise NotFound("User is not a member of this group.")

class CreateAdminView(generics.CreateAPIView):
    queryset = GroupAdmin.objects.all()
    serializer_class = GroupAdminSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        group_id = self.kwargs['group_id']
        group = Group.objects.get(id=group_id)
        serializer.save(user=user, group=group)

class RemoveAdminView(generics.DestroyAPIView):
    queryset = GroupAdmin.objects.all()
    serializer_class = GroupAdminSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        group_id = self.kwargs['group_id']
        try:
            return GroupAdmin.objects.get(user=user, group_id=group_id)
        except GroupAdmin.DoesNotExist:
            raise NotFound("Admin does not exist in this group.")

class CreatePostView(generics.CreateAPIView):
    queryset = GroupPost.objects.all()
    serializer_class = GroupPostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

class RemovePostView(generics.DestroyAPIView):
    queryset = GroupPost.objects.all()
    serializer_class = GroupPostSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        post_id = self.kwargs['post_id']
        try:
            post = GroupPost.objects.get(id=post_id)
            if post.user != self.request.user and not self.request.user.groups.filter(name='Super Admin').exists():
                raise permissions.PermissionDenied("You do not have permission to delete this post.")
            return post
        except GroupPost.DoesNotExist:
            raise NotFound("Post does not exist.")

class EditPostView(generics.RetrieveUpdateAPIView):
    queryset = GroupPost.objects.all()
    serializer_class = GroupPostCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        post_id = self.kwargs['post_id']
        try:
            post = GroupPost.objects.get(id=post_id)
            if post.user != self.request.user and not self.request.user.groups.filter(name='Super Admin').exists():
                raise permissions.PermissionDenied("You do not have permission to edit this post.")
            return post
        except GroupPost.DoesNotExist:
            raise NotFound("Post does not exist.")

class EditGroupView(generics.RetrieveUpdateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        group_id = self.kwargs['group_id']
        try:
            group = Group.objects.get(id=group_id)
            if not self.request.user.groups.filter(name='Super Admin').exists():
                raise permissions.PermissionDenied("You do not have permission to edit this group.")
            return group
        except Group.DoesNotExist:
            raise NotFound("Group does not exist.")

class AllGroupsView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

class PublicGroupsView(generics.ListAPIView):
    queryset = Group.objects.filter(group_type='public')
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class PrivateGroupsView(generics.ListAPIView):
    queryset = Group.objects.filter(group_type='private')
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class GroupMemberListView(generics.ListAPIView):
    serializer_class = GroupMemberSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        group_id = self.kwargs.get('group_id')
        return GroupMember.objects.filter(group_id=group_id)
    
class GroupPostListView(generics.ListAPIView):
    serializer_class = GroupPostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        group_id = self.kwargs.get('group_id')
        if not GroupPost.objects.filter(group_id=group_id).exists():
            raise NotFound("Group not found")
        return GroupPost.objects.filter(group_id=group_id)