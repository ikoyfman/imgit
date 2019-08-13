from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

import pdb

from imgit_app.models import (
    Comment,
    Gallery,
    Image,
    Upvote,
    User,
)

# Tests Below


class ImgitTestCase(TestCase):

    def setUp(self):
        # SETUP USERS AND TOKENS
        self.user_1 = User.objects.create(username='test')
        self.user_1.set_password('test')
        self.user_1.save()
        self.token_user1 = Token.objects.create(user=self.user_1)

        self.admin = User.objects.create(username='admin', is_staff=True)
        self.admin.set_password('admin')
        self.admin.save()
        self.token_admin = Token.objects.create(user=self.admin)
        
        # Setup Content Galleries
        self.gallery100 = Gallery.objects.create(
            title="test_gallery100",
            author = self.user_1
        )
        self.gallery100.save()
        self.gallery200 = Gallery.objects.create(
            title="test_gallery200",
            author = self.admin        
        )
        self.gallery200.save()

#         # Setup Content Images
#         self.image1_gallery100 = Image.objects.create(
#             gallery_id = gallery100,
#             img = 
#         )

    def test_user_no_auth(self):
        """ SHOULD Error when not authenticated """
        response = self.client.get('/api/users/')
        expected = {'detail': 'Authentication credentials were not provided.'}
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), expected)
        

    def test_user_no_auth_gallery_view(self):
        """ SHOULD Error when not authenticated """
        response = self.client.get('/api/galleries/')
        expected = {'detail': 'Authentication credentials were not provided.'}
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)
        