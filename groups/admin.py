from django.contrib import admin
from .models import Group,GroupAdmin,GroupMember,GroupPost,GroupPostImage

admin.site.register(Group)
admin.site.register(GroupMember)
admin.site.register(GroupAdmin)
admin.site.register(GroupPost)
admin.site.register(GroupPostImage)
