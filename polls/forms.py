from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    # Define choices for the quantity field
    QUANTITY_CHOICES = [(str(i), str(i)) for i in range(1, 11)]  # 1 to 10

    # Use ChoiceField for the quantity field
    quantity = forms.ChoiceField(choices=QUANTITY_CHOICES, label='Quantity')

    class Meta:
        model = Ticket
        fields = ['movie', 'showtime', 'type', 'quantity']