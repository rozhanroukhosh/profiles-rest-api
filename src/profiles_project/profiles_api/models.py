from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager



# Create your models here.
class UserProfileManager(BaseUserManager):
	"""helps django work with our customer user model."""

	def create_user(self, email, name, password=None):
	   """create a new user profile object"""
	   if not emial:
	   	raise ValueError("user must have an email address.")
	   email=self.normalize_email(email)
	   user=self.models(email=email,name=name)
	   user.set_password(password)
	   user.save(using=self._db)
	   return user

	def create_superuser(self, email, name, password):
	   """"create and save a new superuser with given detail"""
	   user=self.craete_user(email,name,password)
	   user.is_superuser=True
	   user.is_stuff=True
	   user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""represent a user profile inside our system"""
	email = models.EmailField(max_length=255,unique=True)
	name=models.CharField(max_length=255)
	is_active=models.BooleanField(default=True)
	is_stuff=models.BooleanField(default=False)

	objects=UserProfileManager()

	USERNAME_FIELD='email'
	REQUIRED_FIELDS=['name']


	def get_full_name(self):
		"""used to get a user full name."""
		return self.name

	def get_short_name(self):
		""" used to get user short name"""
		return self.name


	def __str__(self):
		"""django when it needs to convert an object to string"""
		return self.email
