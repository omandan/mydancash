from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Contact(models.Model):
	account=models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50,null=False)
	last_sync=models.DateTimeField(default=timezone.now)

	