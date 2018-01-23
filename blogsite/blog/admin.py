from django.contrib import admin
from .models import Post, Comment
from embed_video.admin import AdminVideoMixin

from django.contrib.auth.models import Group


class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Post)

admin.site.register(Comment)

admin.site.unregister(Group)