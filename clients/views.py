from django.shortcuts import render
from django.views import generic
from .models import *
from django.contrib import messages


def HomePage(request):
    return render(request, 'app/home.html')


class ThankYouView(generic.TemplateView):
    template_name = ('components/thank_you.html')