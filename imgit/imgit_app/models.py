from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    # auto_now_add is for creation
    # auto_now is for updated
    modified_on = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)


class Comment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    text = models.TextField(null=False)
