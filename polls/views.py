from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import TicketType, Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    # Your view logic here
    return render(request, 'polls/index.html')  # Change 'polls/index.html' to your actual template path

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return render(request, 'registration/register.html', {'registration_success': True})
        else:
            for error in form.errors.values():
                messages.error(request, error[0])
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful. Welcome back!')
            return redirect('index')  # Redirect to your index page
        else:
            messages.error(request, 'Login failed. Please check your username and password.')
    return render(request, 'registration/login.html')

def showtimes(request):
    # Add logic to retrieve actual showtime data from your database
    showtime_data = [
        {"movie": "ALL MOVIES", "time": "11:00AM | 2:00PM | 6:00PM | 9:00PM | 11:00PM"},
    ]

    return render(request, 'polls/showtimes.html', {'showtime_data': showtime_data})

def menu(request):
    # Add logic to retrieve actual menu data from your database
    menu_data = [
        {"item": "Burger", "price": 10.99},
        {"item": "Popcorn", "price": 5.99},
        {"item": "Pizza", "price": 12.99},
        # Add more menu items as needed
    ]

    return render(request, 'polls/menu.html', {'menu_data': menu_data})


def tickets(request):
    ticket_data = Ticket.objects.all()
    form = TicketForm()
    ticket_submitted = False

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            ticket_submitted = True
            form = TicketForm()  # Reset the form after successful submission

    return render(
        request,
        'polls/tickets.html',
        {'ticket_data': ticket_data, 'form': form, 'ticket_submitted': ticket_submitted}
    )

@login_required
def tickets(request):
    ticket_data = Ticket.objects.all()
    form = TicketForm()
    ticket_submitted = False

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            ticket_submitted = True
            form = TicketForm()  # Reset the form after successful submission

    return render(request, 'polls/tickets.html', {'ticket_data': ticket_data, 'form': form, 'ticket_submitted': ticket_submitted})

def contact(request):
    return render(request, "polls/contact.html")