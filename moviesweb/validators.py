from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


def validate_year(value):
    if value > 2022:
        raise ValidationError(_("Niepoprawny rok"))

    return value
