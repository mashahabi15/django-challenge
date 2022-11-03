from typing import Any, Dict

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from selling_platform.enums.response_notification_enums import ResponseNotificationType
from selling_platform.utils.response_utils import ResponseUtils
from users.serializers.sign_up_serializer import SignUpSerializer


class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer
    permission_classes = [
        AllowAny,
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            status_code: int = status.HTTP_201_CREATED
            status_type = ResponseNotificationType.success.value
            data: dict = serializer.data
            message: str = "Your account created successfully."

        else:
            status_code: int = status.HTTP_400_BAD_REQUEST
            status_type = ResponseNotificationType.error.value
            data: dict = serializer.errors
            message: str = "Cannot create account at the moment."

        final_data: Dict[str, Any] = ResponseUtils().get_final_response_result(
            code=status_code,
            status=status_type,
            data=data,
            message=message,
        )

        return Response(data=final_data, status=status_code)
