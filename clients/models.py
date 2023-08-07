from django.db import models



class Client_Number(models.Model):
	Client_Number = models.IntegerField(default=12345, primary_key=True)
	created_at = models.DateField(auto_now_add=True)
	
	def __str__(self):
		return self.Client_Number

class Client(models.Model):
	created_at = models.DateField(auto_now_add=True)
	client_number = models.ForeignKey(Client_Number, on_delete=models.SET_NULL, blank=False, null=True, )
	contact_person = models.BooleanField(default=False, blank=False, null=True )
	first_name = models.CharField(max_length=50, blank=False, null=True)
	last_name =  models.CharField(max_length=50, blank=False, null=True)
	birthday = models.DateField(auto_now=False, null=True, blank=True)
	anniversary = models.DateField(auto_now=False, null=True, blank=True)
	email =  models.CharField(max_length=100, blank=False, null=True)
	phone = models.CharField(max_length=15, blank=False, null=True)
	address =  models.CharField(max_length=100, blank=False, null=True)
	city =  models.CharField(max_length=50, blank=False, null=True)
	state =  models.CharField(max_length=50, blank=False, null=True)
	zipcode =  models.CharField(max_length=20, blank=False, null=True)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}", {self.client_number})
	

class Session_Number(models.Model):
	Session_Number = models.CharField(primary_key=True, default=12345)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.Session_Number
	
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
	date = models.DateField(auto_now_add=False, blank=False, null=True)
	session_number = models.ForeignKey(Session_Number, on_delete=models.SET_NULL, null=True )
	client_number = models.ForeignKey(Client_Number, on_delete=models.SET_NULL, null=True )
	type = models.CharField(max_length=100,choices=SESSION_TYPE, blank=False, null=True)
	location = models.CharField(max_length=100, null=True, blank=True)
	address = models.CharField(max_length=100, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True, default='Indianapolis')
	state = models.CharField(max_length=100, null=True, blank=True, default='Indiana')
