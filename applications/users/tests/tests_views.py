USER_TEST_EMAIL_ADDRESS = "alex@alex.com"

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test.utils import override_settings

from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class CreateSingleUserDjoserTest(APITestCase):
    def setUp(self):
        """Set up a method which is used to initialize before any test run"""
        self.user_info = self.generate_user_info()
        self.invalid_user_info = self.generate_invalid_user_info()
        self.user_url = reverse("customuser-list")

    def generate_user_info(self) -> dict:
        """Generate agent info"""
        return {
            "email": USER_TEST_EMAIL_ADDRESS,
            "birth": "1999-12-02",
            "first_name": "Alex",
            "last_name": "Cuenca",
            "phone": "0989181061",
            "gender": "MAL",
            "username": "AlexAgent",
            "password": "randompassword123",
            "re_password": "randompassword123",
        }

    def generate_invalid_user_info(self) -> dict:
        """Generate invalid agent info"""
        return {
            "birth": "1999-12-02",
            "first_name": "Alex",
            "last_name": "Cuenca",
            "phone": "0989181061",
            "gender": "MAL",
            "username": "AlexAgent",
            "password": "randompassword123",
            "re_password": "randompassword123",
        }

    def test_create_invalid_user_djoser(self):
        """Test for create invalid user with djoser"""
        response = self.client.post(
            self.user_url, self.invalid_user_info, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user(self):
        """Test for create user with djoser"""
        response = self.client.post(self.user_url, self.user_info, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, USER_TEST_EMAIL_ADDRESS)


@override_settings(EMAIL_BACKEND="django.core.mail.backends.console.EmailBackend")
class LoginUserDjoserTest(APITestCase):
    def setUp(self):
        """Set up a method which is used to initialize before any test run"""
        self.user_info = self.generate_user_info()
        self.invalid_user_info = self.generate_invalid_user_info()
        self.user_login_info = self.generate_user_login_info()
        self.user_url = reverse("customuser-list")
        self.jwt_create_url = reverse("jwt-create")

    def generate_user_info(self) -> dict:
        """Generate user info"""
        return {
            "email": USER_TEST_EMAIL_ADDRESS,
            "birth": "1999-12-02",
            "first_name": "Alex",
            "last_name": "Cuenca",
            "phone": "0989181061",
            "gender": "MAL",
            "username": "AlexAgent",
            "password": "randompassword123",
            "re_password": "randompassword123",
        }

    def generate_invalid_user_info(self) -> dict:
        """Generate invalid user info"""
        return {
            "birth": "1999-12-02",
            "first_name": "Alex",
            "last_name": "Cuenca",
            "phone": "0989181061",
            "gender": "MAL",
            "username": "AlexAgent",
            "password": "randompassword123",
            "re_password": "randompassword123",
        }

    def generate_user_login_info(self) -> dict:
        """Generate user login info"""
        return {
            "email": USER_TEST_EMAIL_ADDRESS,
            "password": "randompassword123",
        }

    def test_login_user_djoser(self) -> None:
        user = self.client.post(self.user_url, self.user_info, format="json")
        self.assertEqual(user.status_code, status.HTTP_201_CREATED)

        user_data = User.objects.get(email=USER_TEST_EMAIL_ADDRESS)
        user_data.is_active = True
        user_data.save()

        response = self.client.post(
            self.jwt_create_url, self.user_login_info, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
