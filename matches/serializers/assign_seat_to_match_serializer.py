from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from matches.constants.match_seat_constants import MatchSeatConstants
from matches.models import Match
from matches.models.match_seat import MatchSeat
from stadiums.models import Seat


class AssignSeatToMatchSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate_match(value: Match):
        if value.match_duration or value.match_time < timezone.now():
            raise ValidationError(_("Match has been held."))

        return value

    def validate(self, attrs):
        match: Match = attrs.get(MatchSeatConstants.match)
        seat: Seat = attrs.get(MatchSeatConstants.seat)

        if match.stadium != seat.stadium:
            raise ValidationError(_("This seat doesn't belong to the stadium."))

        return attrs

    class Meta:
        model = MatchSeat
        fields = [
            MatchSeatConstants.match,
            MatchSeatConstants.seat,
        ]
