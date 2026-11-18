from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, RegexValidator

class User(AbstractUser):
    pass
class Specialty(models.Model):
    name = models.CharField(max_length=100)
phone_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="Le téléphone doit contenir 8 chiffres."
)
class Doctor(User):
    license_number = models.CharField(
        max_length=6, unique=True,
        validators=[MaxLengthValidator(6)]
    )
    phone = models.CharField(max_length=8 , validators=[phone_validator])
    specialties = models.ManyToManyField(Specialty, related_name='doctors')
class Patient (User):
    national_id = models.CharField(
        max_length=8, unique=True,
        validators=[RegexValidator(
            r"^\d{8}$", message="La CIN doit contenir 8 chiffres."
        )]
    )
    phone = models.CharField(max_length=8 , validators=[phone_validator])
    birth_date = models.DateField()
