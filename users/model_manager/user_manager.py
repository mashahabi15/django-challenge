from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as DjangoUserManager

from selling_platform.model_manager.base_manager import BaseManager


class UserManager(BaseManager, DjangoUserManager):
    """
    Customized UserManager adapted to the removal of 'username' field.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_user(self, username=None, email=None, password=None, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set.')

        email = self.normalize_email(email)
        user_model = get_user_model()
        user = user_model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
