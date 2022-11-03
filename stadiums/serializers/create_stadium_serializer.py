from rest_framework import serializers

from stadiums.constants.seat_constants import SeatConstants
from stadiums.constants.stadium_constants import StadiumConstants
from stadiums.models import Stadium, Seat
from stadiums.serializers.seats_serializer import SeatsSerializer


class CreateStadiumSerializer(serializers.ModelSerializer):
    """
    A serializer class for creating new stadium
    """
    seats = SeatsSerializer(many=True, allow_null=True)

    def create(self, validated_data):
        seats = validated_data.pop(StadiumConstants.seats)
        stadium = super().create(validated_data=validated_data)
        objs_list: list = [
            Seat(section=item.get(SeatConstants.section), seat_num=item.get(SeatConstants.seat_num), stadium=stadium)
            for item in seats
        ]

        Seat.objects.bulk_create(objs_list)

        return stadium

    class Meta:
        model = Stadium
        fields = [
            StadiumConstants.name,
            StadiumConstants.city,
            StadiumConstants.seats,
        ]
