from django.db import models

# Create your models here.

class Venue(models.Model):
      name = models.CharField('Venue Name', max_length = 120)
      address = models.CharField(max_length = 300)
      zip_code = models.CharField(max_length = 15)
      phone = models.CharField('Contact Phone', max_length = 50)
      web = models.URLField('Website Address')
      email_address = models.EmailField('Email Address')
      
      def __init__(self):
            return self.name
      
class MyClubUser(models.Model):
      first_name = models.CharField('Venue Name', max_length = 120)
      last_name = models.CharField('Venue Name', max_length = 120)
      email = models.EmailField('User Email')
      def __init__(self):
            return self.first_name + ' ' + self.last_name


class Event(models.Model):
      name = models.CharField('Event Name', max_length = 120)
      event_date = models.DateTimeField('Event Date')
      venue = models.ForeignKey(Venue, blank = True, null = True, on_delete = models.CASCADE)
      #venue = models.CharField(max_length= 120)
      manager = models.CharField(max_length = 120)
      description = models.TextField(blank = True)
      attendees = models.ManyToManyField(MyClubUser, blank = True)

      def __init__(self):
            return self.name