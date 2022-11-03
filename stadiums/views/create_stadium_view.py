from typing import Dict, Any

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from selling_platform.enums.response_notification_enums import ResponseNotificationType
from selling_platform.security.superuser_permission import IsSuperuser
from selling_platform.utils.response_utils import ResponseUtils
from stadiums.serializers.create_stadium_serializer import CreateStadiumSerializer


class CreateStadiumView(CreateAPIView):
    serializer_class = CreateStadiumSerializer

    permission_classes = [
        IsAuthenticated,
        IsSuperuser,
    ]

    def post(self, request, *args, **kwargs):
        serializer: CreateStadiumSerializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            data: dict = serializer.data
            status_code: int = status.HTTP_201_CREATED
            status_type = ResponseNotificationType.success.value
            message: str = "New stadium created successfully."

        else:
            data: dict = serializer.errors
            status_code: int = status.HTTP_400_BAD_REQUEST
            status_type = ResponseNotificationType.error.value
            message: str = "Cannot create new stadium."

        final_data: Dict[str, Any] = ResponseUtils().get_final_response_result(
            code=status_code,
            status=status_type,
            data=data,
            message=message,
        )

        return Response(data=final_data, status=status_code)
