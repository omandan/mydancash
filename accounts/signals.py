from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=User)
def create_Account(sender, instance, created, **kwargs):
	print("user is created")
	if created:
		Account.objects.create(user=instance)
		instance.account.save()

