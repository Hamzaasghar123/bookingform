from django.db import models


class Booking(models.Model):
    eventName = models.CharField(max_length=100)
    eventDate = models.DateField()
    eventTime = models.TimeField()
    eventLocation = models.CharField(max_length=100)
    boothSelect = models.CharField(max_length=100)
    customerContactNumber = models.CharField(max_length=40)
    additionalInfo = models.TextField(blank=True)

    def __str__(self):
        return self.eventName


class Event(models.Model):
    eventName = models.CharField(max_length=100)
    eventDate = models.DateField()
    eventTime = models.TimeField()
    eventLocation = models.CharField(max_length=100)

    def __str__(self):
        return self.eventName
