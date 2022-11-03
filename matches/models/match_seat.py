from django.db import models
from django.db.models import CASCADE

from matches.constants.match_seat_constants import MatchSeatConstants
from selling_platform.models.base import Base


class MatchSeat(Base):
    seat = models.ForeignKey(to='stadiums.seat', on_delete=CASCADE, related_name='assigner_seats')
    match = models.ForeignKey(to='matches.match', on_delete=CASCADE, related_name='matches_seats')

    class Meta:
        verbose_name = 'Match Seat'
        verbose_name_plural = 'Match Seats'
        db_table = 'match_seat'
        # unique_together = [
        #     MatchSeatConstants.match,
        #     MatchSeatConstants.seat,
        # ]
