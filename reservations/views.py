from django.views.generic import DetailView

from reservations.models import Reservation


class ReservationDetailView(DetailView):
    model = Reservation
    template_name = "templates/index.html"

    def get_context_data(self, **kwargs):
        """
        Returns the context data for a view.
        """
        return super().get_context_data(**kwargs)
