from django.db import models
from transferes.models import *
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Bill(models.Model):
	source=models.ForeignKey(User, on_delete=models.CASCADE)
	create_date=models.DateTimeField(default=timezone.now)
	exp_date=models.DateTimeField(null=True)
	vsbilty=models.BooleanField(default=True)
	ammount=models.DecimalField(max_digits=16, decimal_places=3)

	#function for payed bill or not by filtering transfere table

	def valid_exp_date(self):
		if (self.exp_date>self.create_date) :
			return True  
		else:
			return False

	def repayments(self):
		return Transfere.Objects.filter(bill=self, receiver=self.source, create_date__lte=self.exp_date)

	def status(self):
		repayment=0
		for trans in self.repayments():
			if (repayment>=self.ammount):
				return "payed"
			elif (slf.exp_date<timezone.now):
				return "exp"
			repayment+=trans.ammount
		else:
			return "wating"
			
