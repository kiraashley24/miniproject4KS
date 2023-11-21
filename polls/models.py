from django.contrib import admin
from django.db import models

class TicketType(models.Model):
    name = models.CharField(max_length=50, unique=True, default='Standard')

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Showtime(models.Model):
    time = models.CharField(max_length=255)

    def __str__(self):
        return self.time

class Ticket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=1)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, default=1)
    type = models.ForeignKey(TicketType, on_delete=models.CASCADE, default=1)
    quantity = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=50, blank=False, default="John Doe")

    def __str__(self):
        return f"{self.quantity} {self.type.name} ticket(s)"