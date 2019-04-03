from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	send_password = models.CharField(max_length=20)
	send_email = models.CharField(max_length=20)
	email = models.CharField(max_length=30)
	status = models.IntegerField()


class Relationship(models.Model):
	username = models.CharField(max_length=20)
	friend_name = models.CharField(max_length=20)


class Sendemail(models.Model):
	username = models.CharField(max_length=20)
	theme = models.CharField(max_length=20)
	content = models.CharField(max_length=1000)
	time = models.CharField(max_length=100)
	sendto = models.CharField(max_length=20)
	_from = models.CharField(max_length=20)
	status = models.IntegerField()

