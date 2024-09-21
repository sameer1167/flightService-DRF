from django.db import models

# Create your models here.
class Flight(models.Model):
    FlightNumber=models.CharField(max_length=10)
    OperatingAirlines=models.CharField(max_length=10)
    DepartureCity=models.CharField(max_length=10)
    ArivalCity=models.CharField(max_length=10)
    DateOfDeparture=models.DateField()
    EstimatedTimeOfDeparture=models.TimeField()

class Passenger(models.Model):
    FirstName=models.CharField(max_length=20)
    MiddleName=models.CharField(max_length=20)
    LastName=models.CharField(max_length=20)
    PhoneNumber=models.CharField(max_length=10)
    Email=models.EmailField()

class Reservation(models.Model):
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger=models.ForeignKey(Passenger,on_delete=models.CASCADE)