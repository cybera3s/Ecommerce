from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('user', 'product', 'is_reply', 'reply', 'body', 'can_publish')
    list_display = ('user', 'product', 'is_reply', 'can_publish')
    raw_id_fields = ('user', 'product', 'reply',)
    search_fields = ('user', 'body')
    list_editable = ('can_publish',)
