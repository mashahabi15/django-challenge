from django.urls import path

from matches.views.create_match_view import CreateMatchView

urlpatterns = [

    path('create/', CreateMatchView.as_view(), name="create_match"),

]
