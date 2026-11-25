from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

class User(AbstractUser):
    pass
class Speciality(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
            verbose_name = 'Speciality'
            verbose_name_plural = 'Specialities'
    def __str__(self):
        return self.name


phone_validator = RegexValidator(
    regex=r"^\d{8}$",
    message="Le téléphone doit contenir 8 chiffres."
)
class Doctor(User):
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    license_number = models.CharField(
        max_length=6, unique=True,
        validators=[MaxLengthValidator(6)]
    )
    phone = models.CharField(max_length=8 , validators=[phone_validator])
    specialties = models.ManyToManyField(Speciality, related_name='doctors')
    def __str__(self):
            return self.username
def validate_past_date(value):
    if value >= timezone.localdate():
        raise ValidationError("Date invalide")

class Patient (User):
    national_id = models.CharField(
        max_length=8, unique=True,
        validators=[RegexValidator(
            r"^\d{8}$", message="La CIN doit contenir 8 chiffres."
        )]
    )
    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
    phone = models.CharField(max_length=8 , validators=[phone_validator])
    birth_date = models.DateField(
        validators=[validate_past_date])
    def __str__(self):
            return self.username

