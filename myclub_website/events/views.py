from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from.forms import VenueForm
# Create your views here.
def update_venue(request):
   return render (request, 'events\update_venue.html', {})


def search_venues(request):
    if request.method == "POST":
       searched = request.POST["searched"]
       venues = Venue.objects.filter(name__contains = searched)
       return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
     return render(request, 'events/search_venues.html', {})

def show_venue(request, venue_id):
   venue = Venue.objects.get(pk = venue_id)
   return render(request, 'events/show_venue.html',{'venue': venue})


def list_venues(request):
   venue_list = Venue.objects.all()
   return render(request, 'events/venue.html', {'venue_list':venue_list})

def add_venue(request):
    submitted = False
    if request.method == "POST":
       form = VenueForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/add_venue?submitted = True')
    else:
     form = VenueForm
     if 'submitted' in request.GET:
        submitted = True

    return render(request, 'events/add_venue.html', {"form":form, "submitted" : submitted,})

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',{'event_list': event_list})


def home(request, year= datetime.now().year, month = datetime.now().strftime("%B")):
    name = "Suraj"
    month= month.title()
    # Create a custom list of month names starting from January at index 1
    custom_month_names = [None] + list(calendar.month_name)[1:]

    try:
        
        # Convert month from name to number using the custom list
        month_number = custom_month_names.index(month)
        month_number = int(month_number)
    except ValueError:
        # Handle the case where the month name is not valid
        month_number = None
    cal = HTMLCalendar().formatmonth(year,
    month_number)
    #Get Current Year

    now = datetime.now()
    current_day = now.day

    #Get Current Time
    time = now.strftime('%I:%M:%S %p')

    return render(request, 'events/home.html', {'name': name,
                                         'year': year,
                                         'month': month,
                                         'month_number': month_number,
                                         'cal':cal,
                                         'current_day': current_day,
                                         'time':time,
                                         })