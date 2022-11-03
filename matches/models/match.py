from django.db import models
from django.db.models import CASCADE

from selling_platform.models.base import Base


class Match(Base):
    match_time = models.DateTimeField(null=False)
    # match duration in minutes
    match_duration = models.IntegerField(null=True)
    is_selling_ticket_active = models.BooleanField(default=False)
    stadium = models.ForeignKey(to='stadiums.Stadium', on_delete=CASCADE, related_name='matches')
    host_team = models.ForeignKey(to='matches.team', on_delete=CASCADE, related_name='hosting_matches')
    guest_team = models.ForeignKey(to='matches.team', on_delete=CASCADE, related_name='guesting_matches')

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
        db_table = 'match'
