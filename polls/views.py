from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import TicketType, Ticket
from .forms import TicketForm
from django.contrib import messages

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to your index page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def showtimes(request):
    # Add logic to retrieve actual showtime data from your database
    showtime_data = [
        {"movie": "Elf", "time": "11:00AM | 2:00PM | 6:00PM | 9:00PM"},
        {"movie": "Ghostbusters 2", "time": "11:45AM | 2:45PM | 6:45PM | 9:45PM"},
        {"movie": "Saving Private Ryan", "time": "10:45AM | 1:45PM | 4:45PM | 8:45PM"},
        {"movie": "Jurassic Park", "time": "10:00AM | 1:00PM | 4:00PM | 8:00PM"},
        {"movie": "Shrek", "time": "10:30AM | 1:30PM | 4:30PM | 7:30PM"},
        {"movie": "The Silence of the Lambs", "time": "3:00PM | 6:00PM | 9:00PM | 11:00PM"},
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
    ticket_purchase_message = ""

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            ticket_purchase_message = "Thanks for purchasing your tickets. Enjoy your movie!"
            # Optionally, you can redirect to a success page or modify as needed.
            messages.success(request, ticket_purchase_message)

    return render(request, 'polls/tickets.html', {'ticket_data': ticket_data, 'form': form, 'ticket_purchase_message': ticket_purchase_message})


def contact(request):
    return render(request, "polls/contact.html")