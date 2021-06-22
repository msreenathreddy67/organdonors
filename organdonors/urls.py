"""organdonors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views  
from django.urls import path,re_path 
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('home/',views.Home.as_view(),name='home'),
    path('donor/',views.Donor.as_view(),name='donor'), 
    path('hospital/',views.Hospital.as_view(),name='hospital'),  
    path('patient/',views.Patient.as_view(),name='patient'), 
    path('register/',views.register,name='register'), 
    path('pregister/',views.pregister,name='pregister'),
    path('CBVTemp/',TemplateView.as_view(template_name='d.html'),name='CBVTemp'),
    path('prequestregister/',views.prequestregister,name='prequestregister'),
    path('donorlist/',views.DonorRegListView.as_view(),name='donorlist'), 
    path('patientlist/',views.PatientRegListView.as_view(),name='patientlist'),
    path('hospitallist/',views.HospitalListView.as_view(),name='hospitallist'),
    path('select_hospital/',views.select_hospital,name='select_hospital'),
    re_path('donor/(?P<pk>\d+)/',views.DonorRegDetailView.as_view(),name='detail'),
    re_path('patient/(?P<pk>\d+)/',views.PatientRegDetailView.as_view(),name='detailes'), 
    re_path('hospital/(?P<pk>\d+)/',views.HospitalsDetailView.as_view(),name='detailees'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
