from django.db import models
from django.contrib.auth.models import User
from bills.models import *
from django.utils import timezone
class Transfere(models.Model):
	sender= models.ForeignKey(User,related_name='+', on_delete=models.CASCADE)
	receiver= models.ForeignKey(User,related_name='+', on_delete=models.CASCADE)
	ammount=models.DecimalField(max_digits=16, decimal_places=3)
	fee=models.DecimalField(max_digits=16, decimal_places=3)
	create_date = models.DateTimeField(default=timezone.now)
	bill=models.ForeignKey(Bill, on_delete=models.CASCADE)
	
	def fee_calc(self):
		self.fee= self.ammount/100


	def valid_transfere(self):
		if(self.ammount>0 and self.sender.balance>=self.ammount+self.fee):
			return True
		else:
			return False
