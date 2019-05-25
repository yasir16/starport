import re
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_repo_url(value):
    reg = re.compile("^([a-zA-Z\d]{1}[-a-zA-Z\d]*)(/){1}([\-\w]+)$")
    message = _(f"{value} is not a valid username/repo format.")
    if not reg.match(value):
        raise ValidationError(message, code="invalid_format")
        # raise ValidationError(f"{value} is not a valid url to a github repo")


class repo_url_field(forms.CharField):
    def to_python(self, value):
        return value.lower()

    def get_prep_value(self, value):
        return value.lower()

    def get_db_prep_value(self, value, connection, prepared=False):
        return value.lower()

    def validate(self, value):
        # user the parent's handling of required fields, etc
        super().validate(value)

        val = validate_repo_url(value)
