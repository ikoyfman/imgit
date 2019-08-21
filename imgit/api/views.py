from django.contrib.auth.models import User
from imgit_app.models import Comment, Gallery, Image
from api.serializers import (
    CommentSerializer,
    ImageSerializer,
    GallerySerializer,
    UserSerializer
)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import is_author_or_admin

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer

    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly()]
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            permissions += [is_author_or_admin()]
        return permissions


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly()]
        if self.action in ['update', 'partial_update', 'destroy', 'create']:
            permissions += [is_author_or_admin()]
        return permissions


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        permissions = [IsAuthenticatedOrReadOnly()]
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions += [is_author_or_admin()]
        return permissions
