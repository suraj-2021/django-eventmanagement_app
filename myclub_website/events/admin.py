from django.contrib import admin
from .models import MyClubUser
from .models import Venue
from .models import Event
# Register your models here.

admin.site.register(MyClubUser)
admin.site.register(Venue)
admin.site.register(Event)