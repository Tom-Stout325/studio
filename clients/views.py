from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import generic
from .models import *
from django.contrib import messages



def HomePage(request):
	clients = Client.objects.all()
	session = Session.objects.all()
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You Have Been Logged In!")
			return redirect('home')
		else:
			messages.success(request, "There Was An Error Logging In, Please Try Again...")
			return redirect('home')
	else:
		return render(request, 'clients/home.html', {'clients':clients})


def logout_user(request):
	logout(request)
	messages.success(request, "You have signed out.")
	return render(request, 'clients/home.html', {})



class AllClients(generic.ListView):
	model = Client
	template_name = 'clients/clients.html'
	context_object_name = 'clients'


class ClientDetailView(generic.DetailView):
	model = Client
	template_name = 'clients/client.html'
	context_object_name = 'client'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['client'] = Client.objects.all()
		return context
	

class AllSessions(generic.ListView):
	model = Session
	template_name = 'clients/sessions.html'
	context_object_name = 'sessions'


class SessionDetailView(generic.DetailView):
	model = Client
	template_name = 'clients/session.html'
	context_object_name = 'session'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['session'] = Session.objects.all()
		return context