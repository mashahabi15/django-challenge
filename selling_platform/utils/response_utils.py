from typing import Optional

from rest_framework import status as status_code

from selling_platform.constants.response_constants import ResponseConstants
from selling_platform.enums.response_notification_enums import ResponseNotificationType


class ResponseUtils:

    @classmethod
    def get_final_response_result(
            cls,
            code: int = status_code.HTTP_400_BAD_REQUEST,
            status: str = ResponseNotificationType.error.value,
            message: Optional[str] = str(),
            data: Optional[dict] = None) -> dict:

        if data is None:
            data = dict()

        return {
            ResponseConstants.code: code,
            ResponseConstants.status: status,
            ResponseConstants.data: data,
            ResponseConstants.message: message,
        }
