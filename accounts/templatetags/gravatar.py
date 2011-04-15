# Provides a lot of convenient methods for implementing gravatar support.
# Documentation for gravatar @ http://en.gravatar.com/site/implement/hash/

from django import template
from django.template.defaultfilters import stringfilter
import md5

register = template.Library()

@register.filter
@stringfilter
def gravatar_url( email ):
	"""
	Takes an email address and returns the url for that email's gravatar.
	"""
	# Consider allowing args for size/rating for image provied.
	return ('http://gravatar.com/avatar/' + (md5.new(email.lower()).hexdigest()))
gravatar_url.is_safe = True