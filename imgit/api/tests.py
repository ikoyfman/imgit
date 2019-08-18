from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from pathlib import Path

import pdb
from django.core.files.uploadedfile import SimpleUploadedFile
from freezegun import freeze_time

from imgit_app.models import Comment, Gallery, Image, Upvote

# Tests Below


class ImgitTestCase(TestCase):
    @freeze_time("2019-08-14 12:00:00")
    def setUp(self):
        # SETUP USERS AND TOKENS
        self.user_1 = User.objects.create(username="test")
        self.user_1.set_password("test")
        self.user_1.save()
        self.token_user1 = Token.objects.create(user=self.user_1)

        self.admin = User.objects.create(
            username="admin", is_superuser=True, is_staff=True
        )
        self.admin.set_password("admin")
        self.admin.save()
        self.token_admin = Token.objects.create(user=self.admin)

        # Setup Content Galleries
        self.gallery100 = Gallery.objects.create(
            title="test_gallery100", author=self.user_1
        )
        self.gallery100.save()
        self.gallery200 = Gallery.objects.create(
            title="test_gallery200", author=self.admin
        )
        self.gallery200.save()

        # # Setup images
        # temp_path = r'api/temp_files'
        # image1_path = temp_path + '/temp1.gif'
        # image2_path = temp_path + '/temp2.gif'
        # image3_path = temp_path + '/temp3.jpg'

        # self.image1 = Image.objects.create(
        #     gallery_id=self.gallery100,
        #     img=SimpleUploadedFile(
        #         name='temp1.gif',
        #         content=open(image1_path, 'rb').read()
        #         ),
        # )
        # self.image1.save()

        # self.image2 = Image.objects.create(
        #     gallery_id=self.gallery100,
        #     img=SimpleUploadedFile(
        #         name='temp2.gif',
        #         content=open(image2_path, 'rb').read()
        #         ),
        # )
        # self.image2.save()

        # self.image3 = Image.objects.create(
        #     gallery_id=self.gallery200,
        #     img=SimpleUploadedFile(
        #         name='temp3.jpg',
        #         content=open(image3_path, 'rb').read()
        #         ),
        # )
        # self.image3.save()

    def test_user_no_auth_user_view(self):
        """ SHOULD Error when not authenticated """
        response = self.client.get("/api/users/")
        expected = {"detail": "Authentication credentials were not provided."}
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), expected)

    def test_user_auth_user_view(self):
        header_user1 = {
            "HTTP_AUTHORIZATION": "Token {}".format(self.token_user1)
            }
        header_admin = {
            "HTTP_AUTHORIZATION": "Token {}".format(self.token_admin)
            }

        # Test admin view
        response = self.client.get(
            "/api/users/", content_type="application/json", **header_admin
        )
        expected = [
            {
                "url": "http://testserver/api/users/1/",
                "username": "test",
                "email": "",
                "groups": [],
            },
            {
                "url": "http://testserver/api/users/2/",
                "username": "admin",
                "email": "",
                "groups": [],
            },
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

        # Test User View
        response = self.client.get(
            "/api/users/", content_type="application/json", **header_user1
        )
        expected = {
            'detail': 'You do not have permission to perform this action.'
            }
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), expected)

    def test_user_no_auth_gallery_view(self):
        """ SHOULD get all galleries when not authenticated """
        response = self.client.get("/api/galleries/")
        expected = [
            {
                "title": "test_gallery100",
                "author": "http://testserver/api/users/1/",
                "created_on": "2019-08-14T12:00:00Z",
                "modified_on": "2019-08-14T12:00:00Z",
            },
            {
                "title": "test_gallery200",
                "author": "http://testserver/api/users/2/",
                "created_on": "2019-08-14T12:00:00Z",
                "modified_on": "2019-08-14T12:00:00Z",
            },
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_user_auth_gallery_view(self):
        """ Use token to test gallery view """
        header_admin = {
            "HTTP_AUTHORIZATION": "Token {}".format(self.token_admin)
            }
        response = self.client.get("/api/galleries/", **header_admin)
        expected = [
            {
                "title": "test_gallery100",
                "author": "http://testserver/api/users/1/",
                "created_on": "2019-08-14T12:00:00Z",
                "modified_on": "2019-08-14T12:00:00Z",
            },
            {
                "title": "test_gallery200",
                "author": "http://testserver/api/users/2/",
                "created_on": "2019-08-14T12:00:00Z",
                "modified_on": "2019-08-14T12:00:00Z",
            },
        ]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_gallery_creation_no_auth(self):
        

    def test_user_image_upload_post(self):
        header_user1 = {
            "HTTP_AUTHORIZATION": "Token {}".format(self.token_user1)
            }
        img_1_path = Path('/imgit/api/temp_files/temp1.gif')
        # TODO Finish writing test_user_image_upload
