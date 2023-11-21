from django.contrib import admin
from django.db import models
from django.utils import timezone
import datetime
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

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
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True)
    showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(TicketType, on_delete=models.CASCADE, default=1)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} {self.type.name} ticket(s)"