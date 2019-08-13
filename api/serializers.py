from django.contrib.auth.models import User
from imgit.imgit_app.models import Gallery, Image, Comment
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Gallery
        fields = ['title', 'author', 'created_on', 'modified_on']


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ['gallery_id', 'img', 'created_on']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['gallery_id', 'author', 'created_on', 'modified_on']
