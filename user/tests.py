from django.test import TestCase

from user.models import User

class TestUser(TestCase):
    def test_create_user(self):
        user = User(name="Test User")
        user.save()
        self.assertEqual(user.name, "Test User")
