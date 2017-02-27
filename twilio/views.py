from django.views.generic import TemplateView, ListView, CreateView
from .models import SendSMS
from .forms import SendSMSForm, VerifyForm, UpdatedForm
from .utils import send_twilio_message
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
import random
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

class SendSmsCreateView(CreateView):
	model = SendSMS
	form_class = SendSMSForm
	template_name = 'communication/sendsms_form.html'
	success_url = reverse_lazy('send_sms')
 
	def form_valid(self, form):
		number = form.cleaned_data['to_number']
		body = random.randint(1111,9999)
        # call twilio
		sent = send_twilio_message(number, body)
 
        # save form
		send_sms = form.save(commit=False)
		send_sms.from_number = settings.TWILIO_PHONE_NUMBER
		send_sms.sms_sid = sent.sid
		send_sms.account_sid = sent.account_sid
		send_sms.status = sent.status
		send_sms.body = body
		#send_sms.sent_at = now()
		if sent.price:
			send_sms.price = Decimal(force_text(sent.price))
			send_sms.price_unit = sent.price_unit
		send_sms.save()
		return HttpResponseRedirect(send_sms.get_absolute_url())
		return super(SendSmsCreateView, self).form_valid(form)
		
def verify(request, id):
	send_sms = get_object_or_404(SendSMS, id=id)
	form = VerifyForm(request.POST or None)
	form1 = UpdatedForm(request.POST, instance = send_sms)
	if request.method=='POST':
		
		if form.is_valid and form1.is_valid:
			verify_instance = form.save(commit=False)
			#try:
			#	body = request.POST['body']
			#except:
			#	return Response(status=status.HTTP_400_BAD_REQUEST)
				
			if verify_instance.body == send_sms.body:
				verified = form1.save()
				verified.active = True
				verified.created_at = send_sms.created_at
				verified.save()
				verify_instance.save()
				return HttpResponseRedirect(send_sms.get_absolute_url())
			else:
				return HttpResponse("Invalid Pin",  status=403)
				
		else:
			form = VerifyForm()
			form1 = UpdatedForm(instance = send_sms)
		
	context = {
		"form": form,
		"form1":form1,
		"send_sms": send_sms,
		}
	return render(request, "communication/verify.html", context)
		

				
				
				
			
		