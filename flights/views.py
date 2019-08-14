from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from flights.models import Flight, Passengers


def index(request):
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, 'flights/index.html', context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist.")
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passengers.objects.exclude(flights=flight).all()
    }
    return render(request, "flights/flight.html", context)

def book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passengers.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
        return render(request, "flights/error.html", {"message": "No selections"})
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No flight."})
    except Passengers.DoesNotExist:
        return render(request, "flights/error.html", {"message": "No passenger."})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse("flight", args=(flight_id, )))