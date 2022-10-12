from django.db import models


# Create your models here.
class User(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.First_Name} {self.Last_Name}'

class Airport(models.Model):
    City = models.CharField(max_length=30)
    Code = models.CharField(max_length=3)

    def __str__(self):
        return f'{self.City} {self.Code}'

class Trip(models.Model):
    Duration = models.IntegerField()
    Passengers = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.Origin} to {self.Destination}'

class Flight(models.Model):
    Name = models.CharField(max_length=30)
    Pilot = models.ManyToManyField(User)
    Origin = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="departure")
    Destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="arrival")
    Trip = models.ForeignKey(Trip,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Name} {self.Pilot}'








