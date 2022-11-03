from django.urls import path

from users.views.sign_up_view import SignUpView

urlpatterns = [

    path('sign_up/', SignUpView.as_view(), name="user_sign_up"),

]
