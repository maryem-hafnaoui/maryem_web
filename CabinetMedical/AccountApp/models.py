from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
class Speciality(models.Model):
name = models.CharField(max_length=255)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
class User (AbstractUser) :
    pass


class Doctor(User):
license_number = models.CharField(max_length=6, unique=True)
phone = models.CharField(max_length=8)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
# specialities = models.ManyToManyField(“AccountApp.Speciality”)
specialities = models.ManyToManyField(
Speciality,
related_name='doctors',
)

number_validator = RegexValidator(
    regex=r'^\d{8}$',
    message="Le numéro de téléphone doit contenir exactement 8 chiffres.",
)
def validate_birth_date()v:
    if v>= timezone.localdate():
        raise validatorError("la date ne peut pas etre dans le futur")
class Patient(User):
national_id = models.CharField(max_length=8, unique=True)
phone = models.CharField(max_length=8, validators=[number_validator])
birth_date = models.DateField(validators=[validate_birth_date])
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
