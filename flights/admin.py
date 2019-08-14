from django.contrib import admin
from .models import Flight, Airport, Passengers
# Register your models here.
class PassengerInline(admin.StackedInline):
    model = Passengers.flights.through
    extra = 1

class FlightAdmin(admin.ModelAdmin):
    inlines = [PassengerInline]

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Flight, FlightAdmin)
admin.site.register(Airport)
admin.site.register(Passengers, PassengerAdmin)