from django.db import models
from django.utils import timezone

class Trans(models.Model):
	account = models.CharField(max_length = 20, primary_key = True)
	name = models.CharField(max_length = 30)
	email = models.CharField(max_length = 60)
	mobile = models.CharField(max_length = 15)
	balance = models.CharField(max_length = 20)
	date = models.DateField(default=timezone.now)

class Meta:
    db_table = "bank_Trans"		