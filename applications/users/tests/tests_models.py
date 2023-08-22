from django.test import TestCase
from django.contrib.auth import get_user_model

from ..utils import set_age

User = get_user_model()


class UserTest(TestCase):
    """Test module for User model"""

    def setUp(self) -> None:
        """Setup a method wich is used to initialize before any test run"""
        self.user_info = self.generate_user_info()

    def generate_user_info(self) -> dict:
        """Generate a user info dictionary"""
        return {
            "email": "lakiboj883@royalka.com",
            "birth": "1999-12-02",
            "first_name": "Alex",
            "last_name": "Cuenca",
            "phone": "0989181061",
            "gender": "FEM",
            "username": "AlexAgent",
            "password": "randompassword123",
        }

    def test_user_creation(self) -> None:
        """Test for user creation"""

        user = User.objects.create_user(**self.user_info)
        self.assertEqual(user.email, self.user_info["email"])
        self.assertEqual(user.birth, self.user_info["birth"])
        self.assertEqual(user.first_name, self.user_info["first_name"])
        self.assertEqual(user.last_name, self.user_info["last_name"])
        self.assertEqual(user.gender, self.user_info["gender"])
        self.assertEqual(user.age, set_age(self.user_info["birth"]))
        self.assertEqual(user.phone, self.user_info["phone"])
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
