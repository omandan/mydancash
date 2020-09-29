from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from transferes.models import *
from django.utils import timezone
from phone_field import PhoneField
# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
    	return self.user.username

    def balance(self):
    	exports=Transfere.objects.filter(sender=self.user)
    	imports=Transfere.objects.filter(receiver=self.user)
    	balance=0
    	if self.user.is_superuser:
    		fees_imports=(Transfere.objects.filter(fee__gt=0))
    		#and othrer imports
    		for trans in fees_imports:
    			balance+=trans.fee

    	for trans in exports:
    		balance-=trans.ammount
    		if not self.user.is_superuser:
    			balance-=trans.fee 
    	for trans in imports:
    		balance+=trans.ammount


    	return balance

    def save(self, *args, **kawrgs):
	    super().save(*args, **kawrgs)

	    img = Image.open(self.image.path)

	    if img.height > 300 or img.width > 300:
	        output_size = (300, 300)
	        img.thumbnail(output_size)
	        img.save(self.image.path)



class Email(models.Model):
	oner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')
	valid= models.BooleanField(default=False)
	value=models.EmailField(unique=True)

#email log
#

class Phone(models.Model):
	oner=models.ForeignKey(User,on_delete=models.CASCADE)
	valid= models.BooleanField(default=False)
	value= PhoneField(help_text='Contact phone number',unique=True)

class Contact(models.Model):
	oner=models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
	account=models.ForeignKey(User, on_delete=models.CASCADE,related_name='+')
	name = models.CharField(max_length=50,null=False)
	last_sync=models.DateTimeField(default=timezone.now)

