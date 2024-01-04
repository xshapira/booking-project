from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)


class Reservation(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()
    room = models.IntegerField()
