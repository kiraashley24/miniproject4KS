from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    quantity = forms.IntegerField(min_value=1)  # Add this line

    class Meta:
        model = Ticket
        fields = ['type', 'quantity']