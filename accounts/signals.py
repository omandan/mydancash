from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Account,Email,ConfirmEmail
from django.core.mail import send_mail
import secrets
import uuid
import hashlib

@receiver(post_save, sender=User)
def create_Account(sender, instance, created, **kwargs):
	print("user is created")
	if created:
		Account.objects.create(user=instance)
		instance.account.save()

@receiver(pre_save, sender=Email)
def confirm_email(sender, instance, *args, **kwargs):
	is_email_update=True
	try:
		is_email_update=~(instance.value==Email.objects.get(id=instance.id).value)
	except(Email.DoesNotExist):
		is_email_update=True
	if is_email_update:
		instance.valid=False
		key = secrets.token_hex(16)
		salt = uuid.uuid4().hex
		hashed_key = hashlib.sha256(salt.encode() + key.encode()).hexdigest() + ':' + salt
		confirm_email=ConfirmEmail(email=instance,key=hashed_key)
		confirm_massege=send_mail(
            'Confirm Likn',
            'follw this link to confirm your email on Mydan Cash \n http://127.0.0.1:8000/register/id/{0}/token/{1} '.format(confirm_email.id,key),
            'from@example.com',
            [instance.value],
        )
		if confirm_massege:
			print('http://127.0.0.1:8000/register/id/{0}/token/{1}'.format(confirm_email.id,key))#DANGER : ONLY ON DEBUG MODE
			confirm_email.redirct='email-validate'
			confirm_email.status='sent'
			confirm_email.save()
		else:
			confirm_email.redirct='email-validate'
			confirm_email.status='send-failed'
			confirm_email.save()




		