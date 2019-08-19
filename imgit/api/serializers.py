from django.contrib.auth.models import User
from imgit_app.models import Gallery, Image, Comment
from rest_framework import serializers
from rest_framework.validators import ValidationError


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups", "id"]


class GallerySerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):

        # Check if user id is equal object id before creation or if SuperUser
        request = self.context.get("request")
        if request.user.id != data["author"].id and request.user.is_superuser is not True:
            raise ValidationError("Unauthorized User Post")
        return data

    class Meta:
        model = Gallery
        fields = ["title", "author", "created_on", "modified_on", "id"]


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ["gallery_id", "img", "created_on", "id"]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ["created_on", "author", "gallery_id", "text", "prev_comment", "level", "id"]
