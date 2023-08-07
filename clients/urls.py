from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage, name='home'),
    # path('about/', AboutPage, name='about'),
    # path('contact/', ContactPage, name='contact'),
    path('thanks/', ThankYouView.as_view(), name='thanks'),

]