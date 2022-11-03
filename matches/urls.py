from django.urls import path

from matches.views.assign_seat_to_match_view import AssignSeatToMatchView
from matches.views.create_match_view import CreateMatchView

urlpatterns = [

    path('create/', CreateMatchView.as_view(), name="create_match"),
    path('<int:match_id>/assign_seats/', AssignSeatToMatchView.as_view(), name="assign_seats_to_match"),

]
