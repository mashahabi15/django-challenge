from django.db import models
from django.db.models import CASCADE

from selling_platform.models.base import Base


class Seat(Base):
    section = models.CharField(max_length=16, null=False, blank=False)
    seat_num = models.IntegerField(null=False, blank=False)
    stadium_id = models.ForeignKey(to='stadiums.Stadium', on_delete=CASCADE, related_name='seats')

    class Meta:
        verbose_name = 'Seat'
        verbose_name_plural = 'Seat'
        db_table = 'seat'
