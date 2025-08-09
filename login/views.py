from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import auth

from Parking.signup.models import user

def login(request):
    if request.method == "POST":
        email1=request.POST['email']
        pswd1=request.POST['pswd']

        user = auth.authenticate(email=email1,pswd=pswd1)

        if user is None:
            return render(request,'login.html')
        else:
            return render(request,'home.html')
    else:
        return render(request,'login.html')