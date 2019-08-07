from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)
    modified_on = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __repr__(self):
        return self.title

    
class Image(models.Model):
    gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')

    
#TODO: NEED TO MAKE SURE TO HAVE DATE FIELDS