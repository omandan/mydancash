from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from transferes.models import *
from django.utils import timezone
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,null=True , blank=True)
    addres = models.CharField(max_length=50 , blank=True, null=True)
    #balans = models.DecimalField(max_digits=16, decimal_places=3)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')


    def save(self, *args, **kawrgs):
	    super().save(*args, **kawrgs)

	    img = Image.open(self.image.path)

	    if img.height > 300 or img.width > 300:
	        output_size = (300, 300)
	        img.thumbnail(output_size)
	        img.save(self.image.path)
"""
	def balance(self):
		exports=Transfere.Object.filter(sender=self)
		imports=Transfere.Object.filter(receiver=self)
		balance=0
		for trans in exports:
			balance-=trans.ammount+fee
		for trans in imports:
			balance+=trans.ammount
"""