from django.db import models

# Create your models here.

from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

class MyUser(EmailAbstractUser):
	# Custom fields
	date_of_birth = models.DateField('Date of birth', null=True, blank=True)

	# Required
	objects = EmailUserManager()

class Students(models.Model):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=40)

class Teachers(models.Model):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=40)
