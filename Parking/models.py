from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from SPS.views import contact

class user(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True,max_length=255,blank=False,)
    fname = models.CharField(('fname'),max_length=30,blank=False,)
    lname = models.CharField(('lname'),max_length=150,blank=False,)
    contact = models.CharField(('conatct'),max_length=10,blank=False,)
    city = models.CharField(('city'),max_length=25, blank=False,)
    pswd = models.CharField(('pswd'),max_length=25,blank=False,)

class pstorey(models.Model):

    pname = models.EmailField(unique=True,max_length=255,blank=False,)
    padd = models.CharField(('padd'),max_length=255,blank=False,)
    prate = models.CharField(('prate'),max_length=30,blank=False,)
    tslot = models.CharField(('tslot'),max_length=30,blank=False,)
    aslot = models.CharField(('aslot'),max_length=30,blank=False,)

class feedback(models.Model):

    name = models.CharField(('name'),max_length=255,blank=False,)
    contact = models.CharField(('contact'),max_length=255,blank=False,)
    email = models.EmailField(('email'),max_length=255,blank=False,)
    storey = models.EmailField(('padd'),max_length=255,blank=False,)
    feedback = models.CharField(('feedback'),max_length=255,blank=False,)

class pstorey1(models.Model):

    slot = models.CharField(unique=True,max_length=25,blank=False)
    avail = models.BooleanField(blank=False)