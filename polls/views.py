#INF 601 - Advanced Programming in Python
#Kira Selucky
#Mini project 4

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import TicketType, Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
def index(request):
    return render(request, 'polls/index.html')

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
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('polls:tickets') # redirects to tickets page on successful login
        else:
            messages.error(request, 'Login failed. Please check your username and password.') # unsuccessful message

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def showtimes(request):
    showtime_data = [
        {"movie": "ALL MOVIES", "time": "11:00AM | 2:00PM | 6:00PM | 9:00PM | 11:00PM"},
    ]
    return render(request, 'polls/showtimes.html', {'showtime_data': showtime_data})

def menu(request):
    return render(request, 'polls/menu.html')


@login_required(login_url='/login/') # requires login for ticket submission
def tickets(request):
    ticket_data = Ticket.objects.all()
    form = TicketForm()
    ticket_submitted = False

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            ticket_submitted = True
            form = TicketForm()  # reset the form after successful submission

    return render(request, 'polls/tickets.html', {'ticket_data': ticket_data, 'form': form, 'ticket_submitted': ticket_submitted})

def contact(request):
    return render(request, "polls/contact.html")