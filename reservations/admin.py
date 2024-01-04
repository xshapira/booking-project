from django.contrib import admin

from reservations.models import Reservation


@admin.register(Reservation)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "person",
        "date",
        "room",
    )
