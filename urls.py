from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'the_drawing_game.views.home', name='home'),
    # url(r'^the_drawing_game/', include('the_drawing_game.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

	# Accounts
	url(r'^', include('accounts.urls')),
	url(r'^', include('django.contrib.auth.urls')),
	
	# Sentry
	url(r'^sentry/', include('sentry.urls')),
)
