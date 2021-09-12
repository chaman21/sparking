from django.db import models
from django.utils import timezone

class Customer(models.Model):
	account = models.CharField(max_length = 20, primary_key = True)
	name = models.CharField(max_length = 20)
	email = models.CharField(max_length = 50)
	mobile = models.CharField(max_length = 15)
	balance = models.CharField(max_length = 20)
	role = models.CharField(max_length = 10)

class Transact(models.Model):
	account = models.CharField(max_length = 20, primary_key = True)
	name = models.CharField(max_length = 20)
	email = models.CharField(max_length = 50)
	mobile = models.CharField(max_length = 15)
	balance = models.CharField(max_length = 20)
	date = models.DateField(default=timezone.now)
class Meta:
    db_table = "bank_customer"	