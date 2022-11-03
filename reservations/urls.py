from django.urls import path

from reservations.views.reserve_ticket_view import ReserveTicketView

urlpatterns = [

    path('<int:match_id>/reserve/', ReserveTicketView.as_view(), name="reserve_ticket"),

]
