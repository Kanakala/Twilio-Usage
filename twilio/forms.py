from django import forms
from .models import SendSMS, Verify

class SendSMSForm(forms.ModelForm):
 
	class Meta:
		model = SendSMS
		fields = ['to_number', ]
		
class UpdatedForm(forms.ModelForm):
	active = forms.BooleanField(required=False)

	class Meta:
		model = SendSMS
		fields = ['active', ]
		
class VerifyForm(forms.ModelForm):
	class Meta:
		model = Verify
		fields = ['body', ]