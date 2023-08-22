from django.contrib.auth.models import BaseUserManager


class CustomBaseUserManager(BaseUserManager):
    def create_user(self, email: str, username: str, password=None, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        if not username:
            raise ValueError("The username must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self, email: str, username: str, password=None, **extra_fields
    ):
        user = self.create_user(email, username, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user
