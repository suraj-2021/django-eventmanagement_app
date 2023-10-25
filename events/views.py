from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from.forms import VenueForm, EventForm
from django.http import HttpResponse
import csv
# Create your views here.

def venue_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; finename = venues.csv'
    
    #create a csv writer
    writer = csv.writer(response)
    lines = [ ]
    #designate the model
    venues = Venue.objects.all()


    #loop through and output
    for venue in venues:
        lines.append(f'{venue.name}\n {venue.address}\n {venue.phone}\n {venue.email_address}\n')

               

    response.writelines(lines)
    return  response





def venue_text (request):
    response = HttpResponse(content_type ='text/plain')
    response['Content-Disposition'] = 'attachment; finename = venues.txt'
    
    venues = Venue.objects.all()

    #create a blank list
    lines = [    ]

    #loop through and output
    for venue in venues:
        lines.append(f'{venue.name}\n {venue.address}\n {venue.phone}\n {venue.email_address}\n')
       

   # lines = ["This is line 1 \n",
    #         "This is a line 2\n", 
     #        "Thsi is line 3\n",
      #       ]
    
    #write to textfile
    response.writelines(lines)
    return  response

def delete_venue(request, venue_id):
   venue = Venue.objects.get(pk=venue_id)
   venue.delete()
   return redirect('list-venues')
   #return redirect('all-events')


def delete_event(request, event_id):
   event = Event.objects.get(pk=event_id)
   event.delete()
   return render(request, 'events/add_event.html', {'event': event})
   #return redirect('all-events')


def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance = event)
    if form.is_valid():
       form.save()
       return redirect('all-events')
    else:
     return render (request, 'events/update_event.html',{'event': event, 'form' : form} )

def add_event(request):
    submitted = False
    if request.method == "POST":
       form = EventForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/add_event?submitted = True')
    else:
     form = EventForm
     if 'submitted' in request.GET:
        submitted = True
    return render(request, 'events/add_event.html', {'form': form, 'submitted':submitted})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance = venue)
    if form.is_valid():
       form.save()
       return redirect('list-venues')
    else:
     return render (request, 'events/update_venue.html',{'venue': venue, 'form' : form} )


def search_venues(request)  :
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
   venue_list = Venue.objects.all().order_by('name')
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
    event_list = Event.objects.all().order_by('name')
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
