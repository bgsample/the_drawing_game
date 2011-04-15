from django.conf.urls.defaults import patterns, url
from the_drawing_game import settings

urlpatterns = patterns('the_drawing_game.accounts.views',
    url(r'^sign-up/$', 'sign_up', { 
        'template_name': 'accounts/sign_up.html',
        #'SSL': settings.ENABLE_SSL
         }, 'sign_up'
    ),
    
    # url(r'^(?P<username_slug>[-_\w]+)/settings/$', 'settings', { 
    url(r'^settings/$', 'settings', { 
            'template_name': 'accounts/settings.html' 
        }, 'settings'
    ),
    
    # This top page is just a placeholder for now,
    # to be aggregated into another app.
    url(r'^$', 'index', {
            'template_name': 'accounts/index.html'
        }, 'root'
    ),

)

urlpatterns += patterns('django.contrib.auth.views',

	url(r'^settings/change-password/$', 'password_change', {
			'template_name': 'accounts/change_password.html',
			'post_change_redirect': './',
			#'SSL': settings.ENABLE_SSL,
		}, 'change_password'
	),

	url(r'^sign-in/$', 'login', {
			'template_name': 'accounts/sign_in.html',
			#'SSL': settings.ENABLE_SSL,
		}, 'sign_in'
	),
	
	url(r'^sign-out/$', 'logout', {
			'template_name': 'accounts/sign_out.html',
			'next_page': '../',
			#'SSL': settings.ENABLE_SSL,
		}, 'sign_out'
	),

)