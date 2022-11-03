from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from matches.constants.match_seat_constants import MatchSeatConstants
from matches.models import MatchSeat


class ReadMatchSeatSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        match_id: int = attrs.pop(MatchSeatConstants.match)
        seat_id: int = attrs.pop(MatchSeatConstants.seat)

        if not MatchSeat.objects.filter(seat_id=seat_id, match_id=match_id).exists():
            raise ValidationError(_("This seat doesn't belong to this match."))

        return attrs

    class Meta:
        model = MatchSeat
        fields = [
            MatchSeatConstants.match,
            MatchSeatConstants.seat,
        ]
