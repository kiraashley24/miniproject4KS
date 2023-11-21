from django.contrib import admin
from .models import Ticket, Movie, Showtime, TicketType

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(TicketType)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('movie', 'showtime', 'type', 'quantity')

admin.site.register(Ticket, TicketAdmin)