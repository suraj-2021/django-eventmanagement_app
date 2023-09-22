
from django.urls import path
from. import views

urlpatterns = [
  #int = numbers
  #str: strings
  #path = whole Urls/
  #slug: hyphen-and-underscores_stuff
  #UUID = universally unique identifier
     path('', views.home, name = "home"),
     path('<int:year>/<str:month>', views.home, name = "home"),
     path ('events/', views.all_events, name = "all-events"),
     path('add_venue/', views.add_venue, name = 'add-venue'),
     path('list_venues/', views.list_venues, name = 'list-venues'),   
     path('show_venue/<venue_id>', views.show_venue, name = 'show-venue'),

]
