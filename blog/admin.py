from django.contrib import admin
from .models import Post, Comment
from embed_video.admin import AdminVideoMixin


class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass


admin.site.register(Post)

admin.site.register(Comment)
