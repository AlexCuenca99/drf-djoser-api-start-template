import os
from datetime import datetime
from django.conf import settings


def set_age(birth: datetime) -> int:
    current_date = datetime.now()
    birth_date = birth.strptime(str(birth), "%Y-%m-%d")
    age = current_date.year - birth_date.year

    # Verify if not have yet completed year
    if current_date.month < birth_date.month or (
        current_date.month == birth_date.month and current_date.day < birth_date.day
    ):
        age -= 1

    return age


# Image path
def set_image_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "photo_{}.{}".format(instance.id, ext)
    return os.path.join("users", instance.id, "images", "profile", filename)
