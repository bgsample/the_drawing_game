from django.contrib import admin
from the_drawing_game.accounts.models import UserProfile, Friendship

admin.site.register( UserProfile )

class FriendshipAdmin(admin.ModelAdmin):
	list_display = ('id', 'from_user', 'to_user', 'created_at',)

admin.site.register( Friendship, FriendshipAdmin )