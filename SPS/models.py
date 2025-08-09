from django.db import models

class pstorey(models.Model):

    pname = models.CharField(unique=True,max_length=255,blank=False)
    padd = models.CharField(max_length=255,blank=False)
    prate = models.IntegerField(blank=False)
    tslot = models.IntegerField(blank=False)
    def __str__(self):
        return self.pname
    
class feedback(models.Model):

    name = models.CharField(max_length=255,blank=False)
    contact = models.CharField(max_length=255,blank=False)
    email = models.EmailField(max_length=255,blank=False)
    pstorey = models.CharField(max_length=255,blank=False)
    message = models.TextField(blank=False)
    def __str__(self):
        return self.name

class pstorey1(models.Model):

    slot = models.CharField(unique=True,max_length=25,blank=False)
    avail = models.BooleanField(blank=False)
    def __str__(self):
        return self.slot

