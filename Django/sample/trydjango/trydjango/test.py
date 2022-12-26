from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
import os

class TryDjangoConfigTest(TestCase):
    def test_secret_key_strength(self):
        SECRET_KEY = settings.SECRET_KEY
        #SECRET_KEY = os.environ.get("SECRET_KEY")
        # self.assertNotEqual(SECRET_KEY, 'abc123')
        
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Bad secret key {e.messages}"
            self.fail(msg)
