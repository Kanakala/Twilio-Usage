from django.contrib import admin
from django.db import models
from .models import SendSMS, Verify

class SendSMSModelAdmin(admin.ModelAdmin):
    
    class Meta:
            model = SendSMS

admin.site.register( SendSMS, SendSMSModelAdmin)

class VerifyModelAdmin(admin.ModelAdmin):
    
    class Meta:
            model = Verify

admin.site.register( Verify, VerifyModelAdmin)