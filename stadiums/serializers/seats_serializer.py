from rest_framework import serializers

from stadiums.constants.seat_constants import SeatConstants
from stadiums.models import Seat


class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = [
            SeatConstants.section,
            SeatConstants.seat_num,
        ]
