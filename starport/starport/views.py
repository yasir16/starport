from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render
from social_django.models import UserSocialAuth


def home(request):
    return render(request, "home.html")


@login_required
def user_settings(request):
    user = request.user
    try:
        github_login = user.social_auth.get(provider="github")
    except UserSocialAuth:
        github_login = None

    can_disconnect = user.has_usable_password()

    return render(
        request,
        "settings.html",
        {"github_login": github_login, "can_disconnect": can_disconnect},
    )
