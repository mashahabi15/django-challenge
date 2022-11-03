from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from selling_platform.models.base import Base
from users.model_manager.user_manager import UserManager


class User(AbstractBaseUser, Base):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(_('password'), null=True, blank=True, max_length=128)
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    # user object managers
    objects = UserManager()
    all_objects = UserManager(alive_only=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
