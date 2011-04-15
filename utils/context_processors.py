from the_drawing_game import settings

def the_drawing_game( request ):
	return {
		'site_name': settings.SITE_NAME,
		'meta_keywords': settings.META_KEYWORDS,
		'meta_description': settings.META_DESCRIPTION,
		'request': request,
	}
