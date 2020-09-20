from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from bills.models import *
class Pointer(models.Model):
	sender=models.ForeignKey(User,related_name='+', on_delete=models.CASCADE)
	reciver=models.ForeignKey(User,related_name='+', on_delete=models.CASCADE)
	bill=models.ForeignKey(Bill, on_delete=models.CASCADE)
	note = models.CharField(max_length=256,null=True)
	create_date=models.DateTimeField(default=timezone.now)
	see_date=models.DateTimeField(null=True)
		