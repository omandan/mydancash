from django.db import models
from django.contrib.auth.models import User
from bills.models import *
from django.utils import timezone
from django.core import checks
from django.core.exceptions import ValidationError

class Transfere(models.Model):
	sender= models.ForeignKey(User,related_name='+', on_delete=models.DO_NOTHING)
	receiver= models.ForeignKey(User,related_name='+', on_delete=models.DO_NOTHING)
	ammount=models.DecimalField(max_digits=16, decimal_places=3)
	fee=models.DecimalField(max_digits=16, decimal_places=3,blank=True,null=True,)
	create_date = models.DateTimeField(default=timezone.now)
	bill=models.ForeignKey(Bill,blank=True,null=True, on_delete=models.PROTECT)
	
	def fee_calc(self):
		fee=0 if self.sender.is_superuser else self.ammount/100
		return fee

	def clean(self):
		if self.ammount<1 :
			raise ValidationError('ammount not valid')
		if self.sender.is_superuser:
			self.fee=0
		else:
			self.fee=self.fee_calc()
			if self.sender.account.balance()<self.ammount+self.fee :
				raise ValidationError('sender balance is not enough')
	


	def save(self, *args, **kwargs):
		self.full_clean()
		super().save(*args, **kwargs)

	#def add(sender_id,receiver_id,ammount,bill_id=None):
	'''
	@staticmethod
	
		'''