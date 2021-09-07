from django.contrib import admin

from blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'attachment', 'likes_count', 'comments_count')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request):
        return False


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'body')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request):
        return False


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
