from django.conf.urls import include, url
 
from .views import SendSmsCreateView, verify
 
urlpatterns = [
    url(
        regex=r'^communication/send/sms/$',
        view=SendSmsCreateView.as_view(),
        name='send_sms'
    ),
	url(r'^communication/send/verify/(?P<id>[\w-]+)$', verify, name='verify')
]