from django.db import models

from selling_platform.models.base import Base
from stadiums.constants.stadium_constants import StadiumConstants


class Stadium(Base):
    name = models.CharField(max_length=64, null=False, blank=False)
    city = models.CharField(max_length=32, null=False, blank=False)

    class Meta:
        verbose_name = 'Stadium'
        verbose_name_plural = 'Stadiums'
        db_table = 'stadium'
        unique_together = [
            StadiumConstants.name,
            StadiumConstants.city,
        ]
