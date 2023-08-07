from django.db import models



class Client_Number(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	client_number = models.AutoField(primary_key=True)
	
	def __str__(self):
		return self.client_number

class Clients(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	client_number = models.ForeignKey(Client_Number, on_delete=models.SET_NULL, null=True )
	contact_person = models.BooleanField(default=False)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	birthday = models.DateField(auto_now=False, null=True, blank=True)
	anniversary = models.DateField(auto_now=False, null=True, blank=True)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}", {self.client_number})
	

class Session_Number(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	Session_number = models.AutoField(primary_key=True)
	
	def __str__(self):
		return self.session_number
	
class Session(models.Model):
	# PORT, "Portraits",
	# SEN, "Senior Portraits",
	# FAM, "Family Portraits",
	# WED, "Weddings",
	# SPORT, "Sports",
	# EVNT, "Events",
	# DRONE, "Drone Services",
	# HEAD, "Headshots",
	# OTHER, "Other"
   
	SESSION_TYPE= [
		('PORT', "Portraits"),
		('SEN', "Senior Portraits"),
		('FAM', "Family Portraits"),
		('WED', "Weddings"),
		('SPORT', "Sports"),
		('EVNT', "Events"),
		('DRONE', "Drone Services"),
		('HEAD', "Headshots"),
		('OTHER', "Other"),
	]

	created_at = models.DateTimeField(auto_now_add=True)
	date = models.DateTimeField(auto_now_add=False)
	session_number = models.ForeignKey(Session_Number, on_delete=models.SET_NULL, null=True )
	client_number = models.ForeignKey(Client_Number, on_delete=models.SET_NULL, null=True )
	type = models.CharField(max_length=100,choices=SESSION_TYPE)
	location = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True, default='Indianapolis')
	state = models.CharField(max_length=100, null=True, blank=True, default='Indiana')
