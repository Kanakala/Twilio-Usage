from django.db import models
from django.core.urlresolvers import reverse

class SendSMS(models.Model):
	to_number = models.CharField(max_length=30)
	from_number = models.CharField(max_length=30)
	body = models.CharField(max_length=4)
	sms_sid = models.CharField(max_length=34, default="", blank=True)
	account_sid = models.CharField(max_length=34, default="", blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
    #sent_at = models.DateTimeField(null=True, blank=True)
    #delivered_at = models.DateTimeField(null=True, blank=True)
	status = models.CharField(max_length=20, default="", blank=True)
	active = models.BooleanField(default = False)
	
	def __unicode__(self):
		return self.to_number

	def __str__(self):
		return self.to_number
    
	def get_absolute_url(self):
		return reverse("verify", kwargs={"id": self.id})
	
class Verify(models.Model):
	body = models.CharField(max_length=4)
	
	
