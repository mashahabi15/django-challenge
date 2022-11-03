from django.db import models

from selling_platform.models.base import Base


class Team(Base):
    name = models.CharField(max_length=32, null=False, blank=False)
    members_num = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        db_table = 'team'
