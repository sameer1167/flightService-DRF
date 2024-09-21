from django.shortcuts import render
from . models import Flight,Passenger,Reservation
from .serializers import flightSerializer,passengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
def find_flight(request):
    flights=Flight.objects.filter(DepartureCity=request.data['DepartureCity'],ArivalCity=request.data['ArivalCity'],DateOfDeparture=request.data['DateOfDeparture'])
    serializer=flightSerializer(flights,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight= Flight.objects.get(id=request.data['flightId'])

    passenger=Passenger()
    passenger.FirstName = request.data['FirstName']
    passenger.MiddleName = request.data['MiddleName']
    passenger.LastName = request.data['LastName']
    passenger.Email = request.data['Email']
    passenger.PhoneNumber = request.data['PhoneNumber']
    passenger.save()

    reservation=Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=flightSerializer
    permission_classes=(IsAuthenticated,)

class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=passengerSerializer

class ResevationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer