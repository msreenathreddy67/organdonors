from django.shortcuts import render 
from app.forms import *
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

from django.http import HttpResponse 
from django.views.generic import View  
from django.urls import reverse_lazy
class Home(View):
    def get(self,request):
        return render(request,'app/home.html') 

class Donor(View):
    def get(self,request):
        return render(request,'app/donor.html') 


class Hospital(View):
    def get(self,request):
        return render(request,'app/hospital.html') 

class Patient(View):
    def get(self,request):
        return render(request,'app/patient.html') 

def register(request):
    donorreg=DonorRegForm()
    if request.method=='POST' and request.FILES:
        donordata=DonorRegForm(request.POST,request.FILES)
        if donordata.is_valid():
            donordata.save()
            return HttpResponse('user is created Successfully')

    return render(request,'app/register.html',context={'donorreg':donorreg})  




def pregister(request):
    preg=PatientRegForm()
    if request.method=='POST' and request.FILES:
        pdata=PatientRegForm(request.POST,request.FILES)
        if pdata.is_valid():
            pdata.save()
            return HttpResponse('user is created Successfully')

    return render(request,'app/pregister.html',context={'preg': preg})  



def prequestregister(request):
    preqreg=PatientRequestForm()
    if request.method=='POST':
        preqdata=PatientRequestForm(request.POST)
        if preqdata.is_valid():
            preqdata.save()
            return HttpResponse('user is created Successfully')

    return render(request,'app/prequest_register.html',context={'preqreg': preqreg}) 



class DonorRegListView(ListView): 
    model=DonorReg  
    queryset=DonorReg.objects.all()
    context_object_name='donors' 


class PatientRegListView(ListView): 
    model=PatientReg  
    queryset=PatientReg.objects.all()
    context_object_name='patients' 


class HospitalListView(ListView): 
    model=Hopitals 
    queryset=Hopitals.objects.all() 
    context_object_name='Hospital'
    

class HospitalsDetailView(DetailView): 
    model=DonorReg 
    context_object_name='hospital' 


class DonorRegDetailView(DetailView): 
    model=DonorReg 
    context_object_name='donor' 


class PatientRegDetailView(DetailView): 
    model=PatientReg 
    context_object_name='patient'  
    


def select_hospital(request):
   # hospitals=Hopitals.objects.all()
    if request.method=='POST':
        hospitalname=request.POST['hospital']
        hospitalselect=Hopitals.objects.filter(Hospital_Name= hospitalname)
        d={' hospitalselect': hospitalselect}
        return render(request,'display_hospitaldetails.html',context=d)
    
    return render(request,'select_hospital.html',context={'hospitalselect':hospitalselect})
