from django.contrib import admin

from blog.models import (
    Post,
    Category,
    PostImages
)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    list_display = (
        'id_post',
    )