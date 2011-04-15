from pytz import common_timezones
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# offer these programatically
TIME_ZONE_CHOICES = (
	('Tokyo', 'Asia/Tokyo',),
	('New York City', 'America/New_York'),
	('UTC', 'UTC'),
)

class UserProfile( models.Model ):
	"""
	Extends the user model via a one-to-one relationship.
	"""
	bio = models.TextField( blank = True, null = True )
	time_zone = models.CharField( max_length = 100, choices = TIME_ZONE_CHOICES )
	user = models.ForeignKey( User, unique = True )


class FriendshipManager( models.Manager ):
	"""
	Offers methods for conveniently querying friendships among users.
	"""
	def friends_for_user(self, user):
		friends = []
		for friendship in self.filter(from_user=user).select_related(depth=1):
			friends.append({"friend": friendship.to_user, "friendship": friendship})
		for friendship in self.filter(to_user=user).select_related(depth=1):
			friends.append({"friend": friendship.from_user, "friendship": friendship})
		return friends
	
	def are_friends(self, user1, user2):
		if self.filter(from_user=user1, to_user=user2).count() > 0:
			return True
		if self.filter(from_user=user2, to_user=user1).count() > 0:
			return True
		return False
	
	def remove(self, user1, user2):
		if self.filter(from_user=user1, to_user=user2):
			friendship = self.filter(from_user=user1, to_user=user2)
		elif self.filter(from_user=user2, to_user=user1):
			friendship = self.filter(from_user=user2, to_user=user1)
		friendship.delete()

class Friendship( models.Model ):
	to_user = models.ForeignKey( User, related_name = 'friends' )
	from_user = models.ForeignKey( User, related_name = '_unused_')
	created_at = models.DateTimeField( auto_now_add = True, default = datetime.now(), editable = False )
	updated_at = models.DateTimeField( auto_now = True, default = datetime.now(), editable = False )
	objects = FriendshipManager()
	
	class Meta( object ):
		unique_together = (('to_user', 'from_user'),)
	

def friend_set_for(user):
	"""
	Returns a set of friends for any given user.
	"""
	return set([obj["friend"] for obj in Friendship.objects.friends_for_user(user)])
	
	
	
	
	
	