from django.shortcuts import render, HttpResponseRedirect
import logging

logger = logging.getLogger(__name__)


def home(request):
    message = 'You visited from: %s' % request.META.get('REMOTE_ADDR')
    logger.info(message)
    return render(request, 'home.html', {'message': message})


def login(request):
    try:
        next_url = request.GET['next']
    except:
        try:
            next_url = request.POST['next']
        except:
            next_url = '/'
    request.session['login_redirect_url'] = next_url
    return HttpResponseRedirect('/accounts/gitlab/login/?process=login')


def oauth_redirect(request):
    try:
        next_url = request.session['login_redirect_url']
    except:
        next_url = '/'
    return HttpResponseRedirect(next_url)
