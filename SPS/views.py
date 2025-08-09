from distutils.command.config import config
from email import message
from imaplib import _Authenticator
from django.shortcuts import render
from .models import pstorey
from .models import feedback
from .models import pstorey1
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import pyrebase

config={

  "apiKey": "AIzaSyA8JnfQ8M6wsMMcN2CKUgu7D6HtbT_kM5k",
  "authDomain": "fir-2d0b5.firebaseapp.com",
  "databaseURL": "https://fir-2d0b5-default-rtdb.firebaseio.com",
  "projectId" : "fir-2d0b5",
  "storageBucket" : "fir-2d0b5.appspot.com",
  "messagingSenderId" : "536497043393",
  "appId" : "1:536497043393:web:6d00c40b2b1758b9312140",
  "measurementId" : "G-HHDQYVT51D"
}

firebase=pyrebase.initialize_app(config)

database=firebase.database()

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home Page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is About Page")

def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is Contact Page")

def login(request):
    if request.method == 'POST':
    
        lgusername = request.POST['lgusername']
        lgpswd = request.POST['lgpswd']

        user = authenticate( username=lgusername, password=lgpswd)

        if user is not None:
            return render(request, 'home.html') 
        else:
            messages.error(request,'Incorrect Username or Password. Try Again!')
            return render(request, 'login.html')
    else :
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':

        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pswd = request.POST['pswd']

        myuser = User.objects.create_user(username, email, pswd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        return render(request, 'login.html')
    else:
        return render(request, 'signup.html')

def home(request):
    return render(request, 'home.html') 

def ps1(request):
    
    slot1 = database.child('SLOT1').get().val()
    slot2 = database.child('SLOT2').get().val()
    return render(request, 'ps1.html',{
        "slot1": slot1,
        "slot2": slot2,
    })

def ps2(request):
    form = pstorey.objects.get(pk=2)
    context = {'form':form}
    return render(request, 'ps2.html', context)

def ps3(request):
    form = pstorey.objects.get(pk=3)
    context = {'form':form}
    return render(request, 'ps3.html', context)

def ps4(request):
    form = pstorey.objects.get(pk=4)
    context = {'form':form}
    return render(request, 'ps4.html', context)

def ps5(request):
    form = pstorey.objects.get(pk=5)
    context = {'form':form}
    return render(request, 'ps5.html', context)

def ps6(request):
    form = pstorey.objects.get(pk=6)
    context = {'form':form}
    return render(request, 'ps6.html', context)

def ps7(request):
    form = pstorey.objects.get(pk=7)
    context = {'form':form}
    return render(request, 'ps7.html', context)

def feedback(request):
    return render(request, 'feedback.html')

def savefeedback(request):
    if request.method == 'POST':
        email = request.POST['email']
        contact = request.POST['contact']
        pstorey = request.POST['pstorey']
        message = request.POST['message']

        fd = feedback( email=email, contact=contact, pstorey=pstorey, message=message )
        fd.save()

    return render(request, 'feedback.html')

def abc(request):
    return render(request, 'abc.html')

