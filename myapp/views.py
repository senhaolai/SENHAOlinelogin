from django.shortcuts import render,redirect
from allauth.socialaccount.models import SocialAccount, SocialToken
from allauth.socialaccount.providers.line.views import LineOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.socialaccount.providers.oauth2.client import OAuth2Error
from allauth.core.exceptions import ImmediateHttpResponse
from allauth.socialaccount import providers
from allauth.socialaccount.helpers import complete_social_login
from allauth.account.models import EmailAddress
from django.conf import settings
from django.contrib.auth import login

def login(request):
    return render(request, 'login.html')

def line_callback(request):
    adapter = LineOAuth2Adapter()
    try:
        token = adapter.parse_token(request.GET.get('code'))
        app = adapter.get_provider().get_app(request)
        token.app = app
        login_token = adapter.complete_login(request, app, token)
        login_token.account.provider = 'line'
        login_token.account.extra_data = adapter.get_user_info(login_token.token)
        login_token.token = token
        return complete_social_login(request, login_token)
    except OAuth2Error as e:
        raise ImmediateHttpResponse(e)
