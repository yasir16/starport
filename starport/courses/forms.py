import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# from django.core.validators import URLValidator


def validate_repo_url(value):
    reg = re.compile("^([a-zA-Z\d]{1}[-a-zA-Z\d]+)(/){1}([\-\w]+)$")
    message = _(f"{value} not a valid username/repo format.")
    if not reg.match(value):
        raise ValidationError(message, code="invalid_format")
        # raise ValidationError(f"{value} is not a valid url to a github repo")


class AddtoQueueForm(forms.Form):
    repo_url = forms.CharField(
        label="GitHub URL", max_length=100, validators=[validate_repo_url]
    )

