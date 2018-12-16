from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user','nickname', 'title', 'content', 'image_tag', 'thumbnail','created_at']
    list_display_links = ['image_tag']
    readonly_fields = ['image_tag']
