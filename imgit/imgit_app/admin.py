from django.contrib import admin
from .models import Gallery, Image, Comment

# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created_on',
        'modified_on'
    ]

    fields = [
        'title',
        'author',
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
