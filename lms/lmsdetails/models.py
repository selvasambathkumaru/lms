from django.db import models
from django.core.validators import MaxValueValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class EmpDetails(models.Model):
    
    Name = models.CharField(max_length =255)
    empid = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],unique = True)
    designation = models.CharField(max_length =255)
    image = models.ImageField(upload_to ='images/')
    gender = models.CharField(max_length =255)
    eligible_leave = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    Is_employee = models.CharField(max_length =255)
    reporting_to = models.CharField(max_length =255)
    
    def __str__(self):
        return self.Name 
    
class LeaveRequest(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('annual', 'Annual Leave'),
        ('sick', 'Sick Leave'),
        ('casual', 'casual Leave'),
    ]

    employee_name = models.CharField(max_length=255)
    leave_type = models.CharField(choices=LEAVE_TYPE_CHOICES, max_length=20)
    leave_reason = models.CharField(max_length=255)
    requesting_to = models.CharField(max_length=255)
    leave_status = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    cancel_reason = models.CharField(max_length=255, null=True, blank=True)
    lop_status = models.BooleanField(default=False)

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    if created:
        Token.objects.create(user = instance)