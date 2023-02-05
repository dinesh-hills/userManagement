import re
from datetime import date, timedelta
from django.core.exceptions import ValidationError


def validate_only_alphabets(value):
    if not re.search("^[a-zA-Z]+$", value):
        raise ValidationError("This field only accepts alphabets.")


def validate_mobile_number(value: str):
    if not value.isdigit():
        raise ValidationError(f"Please enter only numbers.")

    if len(value) != 10:
        raise ValidationError(
            f"Mobile number must be 10 digits, you have entered {len(value)} digits"
        )


def validate_birthdate_within_150_years(value):
    today = date.today()
    earliest_date = today - timedelta(days=150 * 365)
    if value < earliest_date or value > today:
        raise ValidationError(
            f"Date must be within the last 150 years, between {earliest_date} and {today}."
        )
