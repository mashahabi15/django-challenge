from typing import Any, Dict, List

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from matches.models import MatchSeat
from matches.serializers.read_match_seat_serializer import ReadMatchSeatSerializer
from reservations.serializers.reserve_ticket_serializer import ReserveTicketSerializer
from selling_platform.enums.response_notification_enums import ResponseNotificationType
from selling_platform.utils.response_utils import ResponseUtils


class ReserveTicketView(CreateAPIView):
    serializer_class = ReserveTicketSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        initial_data: List[dict] = self.prepare_data()
        match_seat_serializer = ReadMatchSeatSerializer(data=initial_data, many=True)
        if match_seat_serializer.is_valid():
            for item in initial_data:
                seat = item.pop("seat")
                match = item.pop("match")
                item["match_seat"] = MatchSeat.objects.get(match_id=match, seat_id=seat).pk

            serializer: ReserveTicketSerializer = self.get_serializer(data=initial_data, many=True)
            if serializer.is_valid(raise_exception=False):
                serializer.save()
                data: dict = serializer.data
                status_code: int = status.HTTP_201_CREATED
                status_type = ResponseNotificationType.success.value
                message: str = "Your tickets reserved successfully."

            else:
                data: dict = serializer.errors
                status_code: int = status.HTTP_400_BAD_REQUEST
                status_type = ResponseNotificationType.error.value
                message: str = "Cannot reserve ticket at the moment."

        else:
            data: dict = match_seat_serializer.errors
            status_code: int = status.HTTP_400_BAD_REQUEST
            status_type = ResponseNotificationType.error.value
            message: str = "Cannot reserve ticket at the moment."

        final_data: Dict[str, Any] = ResponseUtils().get_final_response_result(
            code=status_code,
            status=status_type,
            data=data,
            message=message,
        )

        return Response(data=final_data, status=status_code)

    def prepare_data(self) -> List[dict]:
        initial_data: List[dict] = list()

        for item in self.request.data.get("tickets_info"):
            initial_data.append({
                "user": self.request.user.pk,
                "seat": item.get("seat"),
                "match": self.kwargs.get("match_id"),
                "first_name": item.get("first_name"),
                "last_name": item.get("last_name"),
            })

        return initial_data
