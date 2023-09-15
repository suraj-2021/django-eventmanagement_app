from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
# Create your views here.

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