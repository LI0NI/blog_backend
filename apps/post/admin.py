from django.contrib import admin
from .models import Like, Post, PostImage, Tag, Rating

admin.site.register([Tag, Rating, Like])


class TabularInlineImages(admin.TabularInline):
    model = PostImage
    extra = 1
    fields = ["image"]


class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [TabularInlineImages]
    
admin.site.register(Post, PostAdmin)
