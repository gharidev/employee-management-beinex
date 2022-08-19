from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
from django.utils import timezone


# VALIDATORS
def mobile_number_validator(value):
    """Validator method to check wheather the given input is a valid mobile number.""" 
    if not value.isdigit() or (len(value) > 10):
        raise ValidationError('Enter a valid mobile number')


# MODELS
class User(AbstractUser):
    """Custom user model."""

    email = models.EmailField(
        'Email address',
        unique=True,
        error_messages={
            "unique": "A user with that email address already exists.",
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']



class Employee(models.Model):
    """Model class for employee."""

    name = models.CharField('Full name', max_length=20,)
    code = models.CharField('Employee code', max_length=10, unique=True)
    job_title = models.CharField(max_length=30)
    phone = models.CharField(
        max_length=10,
        validators=[mobile_number_validator],
        help_text='Mobile number without country code.'
    )
    email = models.EmailField()
    created_at = models.DateTimeField(default=timezone.now)
    hire_date = models.DateField(null=True, blank=True, help_text='Date on which the employee was hired.')
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        help_text='Net salary of the employee.'
    )
    
    class Meta:
        ordering = ['pk']