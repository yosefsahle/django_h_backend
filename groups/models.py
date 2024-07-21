from django.db import models
from user.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class Group(models.Model):
    GROUP_TYPE_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    group_profile_picture = models.ImageField(upload_to='group/group_profile_pictures/', null=True, blank=True)
    group_name = models.CharField(max_length=255)
    group_description = models.TextField()
    group_type = models.CharField(max_length=10, choices=GROUP_TYPE_CHOICES)
    group_bio = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

class GroupAdmin(models.Model):
    USER_ROLE_CHOICES = [
        ('GSA', 'Group Super Admin'),
        ('GA', 'Group Admin'),
    ]
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_role_on_group = models.CharField(max_length=10, choices=USER_ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.group.group_name} ({self.user_role_on_group})"

class GroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.group.group_name}"

    def save(self, *args, **kwargs):
        is_new_member = self.pk is None
        super().save(*args, **kwargs)
        if is_new_member:
            self.send_join_notification()

    def send_join_notification(self):
        group_admins = GroupAdmin.objects.filter(group=self.group, user_role_on_group='GSA')
        channel_layer = get_channel_layer()
        for admin in group_admins:
            async_to_sync(channel_layer.group_send)(
                f'group_{self.group.id}',
                {
                    'type': 'user_joined',
                    'message': f"{self.user.username} has joined the group {self.group.group_name}."
                }
            )

class GroupPost(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class GroupPostImage(models.Model):
    post = models.ForeignKey(GroupPost,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='group/post_image/')

    def __str__(self):
        return f"Image for {self.post.title}"