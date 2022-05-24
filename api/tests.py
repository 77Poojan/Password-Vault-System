from django.test import TestCase
from api.models import User
from api.utils import decrypt, encrypt

# Create your tests here.
class PasswordTestCase(TestCase):

    def test_encrypted_password(self):
        """Check if encrypted and decrypted password match."""
        user_obj = User.objects.create(email="demo@gmail.com", password="demo@123")
        user_obj.save()
        password = encrypt(user_obj.password)
        self.assertEqual(user_obj.password, decrypt(password))
        