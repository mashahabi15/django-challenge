from django.db import models
from django.db.models import CASCADE

from selling_platform.models.base import Base


class MatchSeat(Base):
    seat = models.ForeignKey(to='stadiums.seat', on_delete=CASCADE, related_name='assigner_seats')
    match = models.ForeignKey(to='matches.match', on_delete=CASCADE, related_name='matches_seats')
    # if user field is filled, then this seat is reserved for this user.
    # I didn't define user-seat relation in another table because I think that would be an over-engineering decision
    user = models.ForeignKey(to='users.user', on_delete=CASCADE, null=True, related_name='user_matches')

    class Meta:
        verbose_name = 'match_seats'
        verbose_name_plural = 'match_seats'
        db_table = 'match_seat'
