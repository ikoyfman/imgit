from django.contrib import admin
from .models import Gallery, Image

# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

#TODO: CHANGE TO REPRESENT ALL MODEL ATTRIBUTES