from django.contrib import admin
from .models import Post, Comment, Rating

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')
    search_fields = ('author__username', 'post__title')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rated_by', 'post', 'rating', 'created_at')
    search_fields = ('rated_by__username', 'post__title', 'rating')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Rating, RatingAdmin)

