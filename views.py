from django.shortcuts import render_to_response, get_object_or_404
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

from the_drawing_game.accounts.forms import CustomUserCreationForm, CustomUserChangeForm

def index( request, template_name = 'accounts/index.html' ):
    """
    Processes requests for the landing page of the site.
    This is merely a placeholder, as the top page will
    likely be handled by another app in the future.
    """
    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )


def sign_up( request, template_name = 'accounts/sign_up.html' ):
    """
    Processes requests for new user registration. If method is being
    accessed via GET, this displays the appropriate form. If via POST,
    this validates request and, after saving the new user in the database,
    logs in the user and redirects to the settings page.
    """
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CustomUserCreationForm( postdata )
        if form.is_valid():
            form.save()
            username = postdata.get( 'username', '' )   # get username, or blank string if not available
            password = postdata.get( 'password1', '' )  # password1 is referenced on django.contrib.auth.forms.py line 17.
                                                        # password2 is the confirmation password input on the form.
            from django.contrib.auth import login, authenticate
            new_user = authenticate( username = username, password = password )
            if new_user and new_user.is_active: # if new_user is not None:
                login( request, new_user )
                url = urlresolvers.reverse( 'settings' )    # redirect to settings page
                return HttpResponseRedirect( url )
    else:   # if request.method == 'GET':
        form = CustomUserCreationForm() # build UserCreationForm()
    page_title = 'Sign Up'
    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )  


def sign_in( request, template_name = 'accounts/sign_in.html' ):
    """
    Processes requests for the settings page, where users
    can edit their profiles.
    """
    return render_to_response( template_name )

    
@login_required 
def settings( request, template_name = 'accounts/settings.html' ):
    """
    Processes requests for the settings page, where users
    can edit their profiles.
    """
    page_title = 'Account Settings'
    # Basic flow is the same as sign_up, above.
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CustomUserChangeForm( postdata, instance = request.user )
        if form.is_valid():
            form.save()
    else:
        form = CustomUserChangeForm( instance = request.user )
    title = 'Settings'
    return render_to_response( template_name, locals(), context_instance = RequestContext( request) )
	
	
	
	
	
