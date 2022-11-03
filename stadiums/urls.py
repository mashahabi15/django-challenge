from django.urls import path

from stadiums.views.create_stadium_view import CreateStadiumView

urlpatterns = [

    path('create/', CreateStadiumView.as_view(), name="create_stadium"),

]
