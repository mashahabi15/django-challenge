from rest_framework import serializers

from stadiums.constants.stadium_constants import StadiumConstants
from stadiums.models import Stadium
from stadiums.serializers.seats_serializer import SeatsSerializer


class CreateStadiumSerializer(serializers.ModelSerializer):
    """
    A serializer class for creating new stadium
    """
    seats = SeatsSerializer(many=True, allow_null=True)

    # todo change here
    class Meta:
        model = Stadium
        fields = [
            StadiumConstants.name,
            StadiumConstants.city,
            StadiumConstants.seats,
        ]
