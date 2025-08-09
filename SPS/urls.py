from django.contrib import admin
from django.urls import path, include
from SPS import views



urlpatterns =[
    path("",views.index, name='index'),
    path("contact",views.contact, name='contact'),
    path("about", views.about, name='about'),
    path("home",views.home, name='home'),
    path("login",views.login,name='login'),
    path("ps1", views.ps1, name='ps1'),
    path("ps2", views.ps2, name='ps2'),
    path("ps3", views.ps3, name='ps3'),
    path("ps4", views.ps4, name='ps4'),
    path("ps5", views.ps5, name='ps5'),
    path("ps6", views.ps6, name='ps6'),
    path("ps7", views.ps7, name='ps6'),
    path("feedback", views.feedback, name='feedback'),
    path("signup",views.signup, name='signup'),
    path("abc", views.abc, name="abc"),
    path("savefeedback", views.savefeedback, name='savefeedback'),
    
] 