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
        self.user_1 = User.objects.create(username='test')
        self.user_1.set_password('test')
        self.user_1.save()
        self.token_user1 = Token.objects.create(user=self.user_1)

        self.admin = User.objects.create(username='admin', is_staff=True)
        self.admin.set_password('admin')
        self.admin.save()
        self.token_admin = Token.objects.create(user=self.admin)

    def test_user_no_auth(self):
        """ SHOULD Error when not authenticated """
        response = self.client.get('/api/users/')
        expected = {'detail': 'Authentication credentials were not provided.'}
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), expected)
