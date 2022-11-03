from rest_framework import serializers

from reservations.constants.ticket_constants import TicketConstants
from reservations.models.ticket import Ticket


class ReserveTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket

        fields = [
            TicketConstants.user,
            "match_seat",
            TicketConstants.first_name,
            TicketConstants.last_name,
        ]
