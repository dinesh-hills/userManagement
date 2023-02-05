from django.db import models

from .validators import (
    validate_birthdate_within_150_years,
    validate_mobile_number,
    validate_only_alphabets,
)


class User(models.Model):
    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_CHOICES = [(GENDER_MALE, "Male"), (GENDER_FEMALE, "Female")]

    first_name = models.CharField(
        max_length=255,
        validators=[validate_only_alphabets],
    )
    last_name = models.CharField(
        max_length=255,
        validators=[validate_only_alphabets],
    )
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(validators=[validate_birthdate_within_150_years])
    mobile_number = models.CharField(max_length=15, validators=[validate_mobile_number])
    address = models.CharField(max_length=500)
