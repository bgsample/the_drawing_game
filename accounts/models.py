from pytz import common_timezones

from django.db import models
from django.contrib.auth.models import User

# offer these programatically
TIME_ZONE_CHOICES = (
	('Tokyo', 'Asia/Tokyo',),
	('New York City', 'America/New_York'),
	('UTC', 'UTC'),
)
     
class UserProfile(models.Model):
    bio = models.TextField( blank = True, null = True )
    time_zone = models.CharField( max_length = 100, choices = TIME_ZONE_CHOICES )
    # friends = models.ManyToManyField( User, blank = True, null = False )
    user = models.ForeignKey(User, unique = True)