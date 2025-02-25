from django.urls import path
from django.views.decorators.cache import cache_page

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', cache_page(60)(views.AboutView.as_view()), name='about'),
    path('contact-information/', cache_page(60)(views.ContactInformationView.as_view()), name='contact_information'),
    path('payment-delivery/', cache_page(60)(views.PaymentDeliveryView.as_view()), name='payment_delivery'),
]