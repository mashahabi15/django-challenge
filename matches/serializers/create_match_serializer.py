import datetime
from datetime import timedelta

from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from matches.constants.match_constants import MatchConstants
from matches.models import Match
from selling_platform.config.general_config import GeneralConfig


class CreateMatchSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        # check if host and guest are not the same
        host_team: int = attrs.get(MatchConstants.host_team)
        guest_team: int = attrs.get(MatchConstants.guest_team)
        match_time: datetime = attrs.get(MatchConstants.match_time)
        stadium: int = attrs.get(MatchConstants.stadium)

        if host_team == guest_team:
            raise ValidationError(_("Host and guest teams are the same."))

        # We assume that each match will be maximum 4 hours and the teams should have at least 2 hours for resting
        match_time_limit_range = (match_time - timedelta(
            hours=GeneralConfig.MAXIMUM_MATCH_DURATION_HOURS + GeneralConfig.MINUMUM_TIME_OF_REST_HOURS,
        ), match_time + timedelta(hours=
                                  GeneralConfig.MAXIMUM_MATCH_DURATION_HOURS - GeneralConfig.MINUMUM_TIME_OF_REST_HOURS,
                                  ))

        # check if host and guest have another match at that time
        if Match.objects.filter(
                host_team=host_team, match_time__range=match_time_limit_range
        ).exists():
            raise ValidationError(_("Host team have another match within this time period"))

        if Match.objects.filter(
                guest_team=guest_team, match_time__range=match_time_limit_range
        ).exists():
            raise ValidationError(_("Guest team have another match within this time period"))

        # check if no other matches are being held in that stadium
        if Match.objects.filter(stadium=stadium, match_time__range=(
                match_time, match_time + timedelta(hours=GeneralConfig.MAXIMUM_MATCH_DURATION_HOURS),
        )):
            raise ValidationError(_("Another match is already set for this time in this stadium."))

        return attrs

    class Meta:
        fields = [
            MatchConstants.match_time,
            MatchConstants.is_selling_ticket_active,
            MatchConstants.stadium,
            MatchConstants.host_team,
            MatchConstants.guest_team,
        ]

        model = Match
