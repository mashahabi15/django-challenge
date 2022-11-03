from django.db import models
from django.db.models import CASCADE

from selling_platform.models.base import Base


class Ticket(Base):
    user = models.ForeignKey(to='users.User', on_delete=CASCADE, related_name='tickets')
    match_seat = models.OneToOneField(to='matches.MatchSeat', on_delete=CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        db_table = 'ticket'
