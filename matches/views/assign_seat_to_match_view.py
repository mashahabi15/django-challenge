from typing import Any, Dict, List

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from matches.constants.match_seat_constants import MatchSeatConstants
from matches.serializers.assign_seat_to_match_serializer import AssignSeatToMatchSerializer
from selling_platform.enums.response_notification_enums import ResponseNotificationType
from selling_platform.security.superuser_permission import IsSuperuser
from selling_platform.utils.response_utils import ResponseUtils


class AssignSeatToMatchView(CreateAPIView):
    serializer_class = AssignSeatToMatchSerializer

    permission_classes = [
        IsAuthenticated,
        IsSuperuser,
    ]

    def post(self, request, *args, **kwargs):
        initial_data: List[dict] = self.prepare_data()
        serializer: AssignSeatToMatchSerializer = self.get_serializer(data=initial_data, many=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            data: dict = serializer.data
            status_code: int = status.HTTP_201_CREATED
            status_type = ResponseNotificationType.success.value
            message: str = "Seats assigned to the match successfully."

        else:
            data: dict = serializer.errors
            status_code: int = status.HTTP_400_BAD_REQUEST
            status_type = ResponseNotificationType.error.value
            message: str = "Cannot assign seats to the match."

        final_data: Dict[str, Any] = ResponseUtils().get_final_response_result(
            code=status_code,
            status=status_type,
            data=data,
            message=message,
        )

        return Response(data=final_data, status=status_code)

    def prepare_data(self) -> List[dict]:
        initial_data: List[dict] = list()

        for seat_id in self.request.data.get('seats'):
            initial_data.append({
                MatchSeatConstants.seat: seat_id,
                MatchSeatConstants.match: self.kwargs.get(MatchSeatConstants.match_id),
            })

        return initial_data
