from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """docstring for ."""
    def create_user_with_email_pass(self):
        email='mahmudnuman@gmail.com'
        password:'123456'
        user=get_user_model().objects.create_user(
        email=email,
        password=password
        )
        self.assertEqual(user.email,  email)
        self.assertTrue(user.check_password(password))
