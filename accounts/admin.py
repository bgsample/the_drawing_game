from django.contrib import admin
from the_drawing_game.accounts.models import UserProfile, Friendship

admin.site.register( UserProfile )
admin.site.register( Friendship )