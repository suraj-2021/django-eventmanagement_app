
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
]