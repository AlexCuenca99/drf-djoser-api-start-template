import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from model_utils.models import TimeStampedModel

from .managers import CustomBaseUserManager
from .choices import GENDER_CHOICES, NONE
from .utils import set_age, set_image_path


class CustomUser(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField("Username", max_length=50, unique=True)
    email = models.EmailField("Email", unique=True, max_length=100)
    is_staff = models.BooleanField("Staff status", default=False)
    is_active = models.BooleanField("Active status", default=True)
    is_admin = models.BooleanField("Admin status", default=False)
    first_name = models.CharField("Last name", max_length=50)
    last_name = models.CharField("First name", max_length=50)
    gender = models.CharField(
        "Gender", max_length=3, choices=GENDER_CHOICES, default=NONE
    )
    age = models.PositiveSmallIntegerField("Age")
    birth = models.DateField("Birth", auto_now=False, auto_now_add=False)
    photo = models.ImageField(
        "Profile photo",
        upload_to=set_image_path,
        height_field=None,
        width_field=None,
        max_length=None,
    )

    objects = CustomBaseUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "birth"]

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def set_age(self, birth):
        self.age = set_age(birth)

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def save(self, *args, **kwargs):
        self.age = set_age(self.birth)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
