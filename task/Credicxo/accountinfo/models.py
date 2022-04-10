from django.db import models

# Create your models here.

from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser

#model for the superuser

class MyUser(EmailAbstractUser):
	
	date_of_birth = models.DateField('Date of birth', null=True, blank=True)

	
	objects = EmailUserManager()

	
#model for the students

class Students(models.Model):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=40)

	
#model for the teachers user 

class Teachers(models.Model):
	email = models.EmailField(unique=True)
	name = models.CharField(max_length=40)
