from django.db import models

from django.urls import reverse

# Create your models here. 

class DonorReg(models.Model):
    Donor_Name=models.CharField(max_length=20)
    Donor_Age=models.PositiveIntegerField() 
    Donation_Item=models.CharField(max_length=20)
    Donor_Phno=models.IntegerField() 
    Donor_Address=models.TextField() 
    Donor_HealthCertificate=models.ImageField(upload_to='Donor_HealthCertificate')  
    

    def __str__(self):
        return self.Donor_Name 
    
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})



class PatientReg(models.Model):
    Patient_Name=models.CharField(max_length=20)
    Patient_Age=models.PositiveIntegerField() 
    Patient_Item=models.CharField(max_length=20)
    Patient_Phno=models.IntegerField() 
    Patient_Address=models.TextField() 
    Patient_HealthCertificate=models.ImageField(upload_to='Donor_HealthCertificate')  
    

    def __str__(self):
        return self.Patient_Name  

    def get_absoulte_url(self):
        return reverse("detailes",kwargs={"pk":self.pk})


class Hopitals(models.Model):
    Hospital_Name=models.CharField(max_length=30)
    Hospital_Loc=models.CharField(max_length=20) 
    Avaliable_Organs=models.CharField(max_length=30) 
    Contact=models.IntegerField()  


    def __str__(self): 
        return self.Hospital_Name 


    def get_absoulte_url(self):
        return reverse("detailees",kwargs={"pk":self.pk})

