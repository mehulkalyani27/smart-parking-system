from django.shortcuts import render
from Parking.Parking.models import user

def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact=request.POST['contact']
        city=request.POST['city']
        email=request.POST['email']
        pswd=request.POST['pswd']
        
        x=user.objects.create_user(fname=fname,lname=lname,contact=contact,city=city,email=email,pswd=pswd)
        x.save()
        
        return render(request,'login.html')
    else:
     return render(request,'signup.html')

     