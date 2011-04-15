from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

class CustomUserCreationForm( UserCreationForm ):
	"""
	Like the UserCreationForm in django.contrib.auth.forms,
	but with an email field.
	"""
	email = forms.EmailField( label = ('E-mail Address'),
	 	help_text = ("We will never give your email to third-parties."),
	 	error_messages = ( {'invalid': ('Please enter a valid email address.') } ) )

	class Meta:
		model = User
		fields = ("username", "email",)


class CustomUserChangeForm( UserChangeForm ):
	class Meta:
		model = User
		fields = ( 'username', 'email', )
