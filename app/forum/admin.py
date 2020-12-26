from django.contrib import admin
from .models import Post, Comment, Category


class PostAdmin(admin.ModelAdmin):
    fields = 'title', 'author', 'category', 'text',
    search_fields = 'title', 'category', 'published',
    list_display = 'title', 'author', 'category', 'published', 'id',
    list_filter = 'title', 'author', 'category', 'published',


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    fields = 'text', 'author', 'post', 'active',
    list_display = 'post', 'author', 'created', 'active', 'updated', 'id',
    list_filter = 'active', 'created', 'author', 'post',
    search_fields = 'author', 'post', 'created',


admin.site.register(Comment, CommentAdmin)

class CategoryAdmin(admin.ModelAdmin):
    fields = 'title',
    list_display = 'title', 'id',
    search_fields = 'title',


admin.site.register(Category, CategoryAdmin)