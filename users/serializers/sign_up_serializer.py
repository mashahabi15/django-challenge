from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from users.constants.user_constants import UserConstants
from users.constants.users_app_constants import UsersAppConstants
from users.model_manager.user_manager import UserManager


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254, min_length=3, required=True, allow_blank=False, allow_null=False)
    repeat_password = serializers.CharField(write_only=True, required=True, allow_blank=False)

    def create(self, validated_data):
        return UserManager().create_user(
            email=self.initial_data.get(UserConstants.email),
            password=self.initial_data.get(UserConstants.password))

    def validate_email(self, value: str) -> str:
        if self.Meta.model.objects.filter(email=value).exists():
            raise serializers.ValidationError(_("A user with this email already exists."))

        return value

    def validate(self, attrs):
        errors: dict = dict()

        password: str = attrs.get(UserConstants.password)
        repeat_password: str = attrs.get(UsersAppConstants.repeat_password)

        if password != repeat_password:
            errors[UsersAppConstants.repeat_password] = _("Password and re-password do not match.")

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    class Meta:
        model = get_user_model()

        fields = [
            UserConstants.email,
            UserConstants.password,
            UsersAppConstants.repeat_password,
            UserConstants.id_key,
        ]

        extra_kwargs = {
            UserConstants.password:
                {
                    'write_only': True,
                    'required': True,
                    'allow_blank': False,
                },
        }
