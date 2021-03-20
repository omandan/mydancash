from django.db import models
from transferes.models import *
from django.contrib.auth.models import User
from django.utils import timezone

#from transferes.models import Transfere

# Create your models here.
class Bill(models.Model):
	source=models.ForeignKey(User, on_delete=models.CASCADE)
	create_date=models.DateTimeField(default=timezone.now)
	exp_date=models.DateTimeField(null=True)
	vsbilty=models.BooleanField(default=True)
	ammount=models.DecimalField(max_digits=16, decimal_places=3)

	#function for payed bill or not by filtering transfere table

	def valid_exp_date(value):
		if (self.exp_date>self.create_date) :
			return True  
		else:
			return False
	
	@staticmethod
	def sended_bill(sender):#add other filter later
		return Bill.objects.filter(source=sender)



