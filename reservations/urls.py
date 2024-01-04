from django.urls import path

from reservations.views import ReservationDetailView

urlpatterns = [
    path("booking/<int:pk>", ReservationDetailView.as_view(), name="reservation"),
]
