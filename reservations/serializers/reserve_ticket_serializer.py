from rest_framework import serializers

from reservations.constants.ticket_constants import TicketConstants
from reservations.models.ticket import Ticket


class ReserveTicketSerializer(serializers.ModelSerializer):
    # def validate(self, attrs):
    #     match_id: int = attrs.pop(MatchSeatConstants.match)
    #     seat_id: int = attrs.pop(MatchSeatConstants.seat)
    #
    #     if not MatchSeat.objects.filter(seat_id=seat_id, match_id=match_id).exists():
    #         raise ValidationError(_("This seat doesn't belong to this match."))
    #
    #     attrs[TicketConstants.match_seat] = MatchSeat.objects.get(seat_id=seat_id, match_id=match_id).pk
    #
    #     return attrs

    class Meta:
        model = Ticket

        fields = [
            TicketConstants.user,
            "match_seat",
            TicketConstants.first_name,
            TicketConstants.last_name,
        ]
