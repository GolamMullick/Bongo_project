
from datetime import timedelta
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import User

from rest_framework import status
from rest_framework.test import APITestCase


class TestRegisterUserAPI(APITestCase):
    def test_post_request_can_register_new_user(self):

        data = {
            "username": "punakepis ",
            "email": "george@gmail.com",
            "mobile_no": "+2404554444",
            "user_type": "admin"

        }
        res = self.client.post(reverse("api:register-user"), data=data)
        status = res.json().get('success')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(status, True)

class TestLoginClientAPI(APITestCase):
    def test_post_request_can_login_user(self):
        user = User.objects.create(
            username='John',
            user_type='Hendrix',
            email='lennon@thebeatles.com'
        )

        user.set_password('johnpassword')
        user.save()
        data = {
            "username": "lennon@thebeatles.com",
            "password": "johnpassword"

        }
        res = self.client.post(reverse("api:login"), data=data)
        status = res.json().get('success')
        self.assertEqual(status, True)
