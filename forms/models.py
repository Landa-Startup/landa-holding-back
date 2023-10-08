from django.db import models
from accounts.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save,pre_save
from uuid import uuid4

# Create your models here.

class StartUpsForm(models.Model):
  firstName=models.CharField(max_length=300,blank=True)
  lastName=models.CharField(max_length=300,blank=True)
  birthDate=models.DateField(blank=True)
  email=models.EmailField(blank=True)
  countryOfResidence=models.CharField(max_length=300,blank=True)
  provinceOfResidence=models.CharField(max_length=300,blank=True)
  type=models.CharField(max_length=300,blank=True)
  ideaExplanation=models.CharField(max_length=300,blank=True)    
  getToKnowUs=models.CharField(max_length=300,blank=True)        
  pitchDeckFile=models.FileField(upload_to='pitchdeckfile',null=True,blank=True,editable=True)      
  businessPlanFile=models.FileField(upload_to='businessPlan',null=True,blank=True,editable=True)
  productName=models.CharField(max_length=500,blank=True)
  siteAddress=models.CharField(max_length=500,blank=True)
  customerProblem=models.TextField(blank=True)
  solution=models.TextField(blank=True)
  productLevel = models.CharField(max_length=200,blank=True)
  scalable=models.TextField(blank=True)
  monetizationOfYourPlan=models.TextField(blank=True)
  structureOfYourSales=models.TextField(blank=True)
  financialModelFile= models.FileField(upload_to='financialModelFile',null=True,blank=True,editable=True)
  cooperatedWithInvestors= models.TextField(blank=True)
  financialFile = models.FileField(upload_to='financialFile',null=True,blank=True,editable=True)
  customerCharacteristic = models.TextField(blank=True)
  currentCustomers = models.TextField(blank=True)
  estimatedMarketSize= models.TextField(blank=True)
  totalTamSamSom = models.TextField(blank=True)
  startupRevenue=models.TextField(blank=True)
  monthlyIncome=models.TextField(blank=True)
  currentInterestRate=models.TextField(blank=True)
  currentRaisedFunding=models.TextField(blank=True)
  neededCapital=models.TextField(blank=True)
  createdAt= models.DateTimeField(auto_now_add=True,blank=True)
  updatedAt= models.DateTimeField(auto_now=True,blank=True)


class ContactUs(models.Model):
  name=models.CharField(max_length=250,blank=True)
  email=models.EmailField(blank=True)
  number=models.CharField(max_length=250,blank=True)
  subject=models.CharField(max_length=500,blank=True)
  message=models.TextField(blank=True)
  createdAt=models.DateTimeField(auto_now_add=True,blank=True)


class PartnerMembership(models.Model):
  firstName=models.CharField(max_length=500, blank=True)
  lastName=models.CharField(max_length=500, blank=True)
  birthDate=models.DateField(blank=True)
  email=models.EmailField(blank=True)
  countryOfResidence=models.CharField(max_length=500, blank=True)
  provinceOfResidence=models.CharField(max_length=500, blank=True)
  companyName=models.CharField(max_length=500, blank=True)
  investmentCeiling=models.CharField(max_length=500, blank=True)
  howDidYouKnowUs=models.CharField(max_length=500, blank=True)
  createdAt=models.DateTimeField(auto_now_add=True, blank=True)     
  updatedAt=models.DateTimeField(auto_now=True, blank=True)

class InvestorRegistration(models.Model):
  firstName=models.CharField(max_length=500, blank=True)
  lastName=models.CharField(max_length=500, blank=True)
  email=models.EmailField(blank=True)
  birthDate=models.DateField(blank=True)
  countryOfResidence=models.CharField(max_length=500, blank=True)
  provinceOfResidence=models.CharField(max_length=500, blank=True)
  companyName=models.CharField(max_length=500, blank=True)
  interestes=models.CharField(max_length=500, blank=True)
  preferredAreas=models.CharField(max_length=500, blank=True)
  howDidYouKnowUs=models.CharField(max_length=500, blank=True)
  createdAt=models.DateTimeField(auto_now_add=True)
  updatedAt=models.DateTimeField(auto_now=True)

class Entrepreuneur(models.Model):
  email = models.EmailField()
  companyName=models.CharField(max_length=300)
  phone=models.CharField(max_length=300)
  website=models.CharField(max_length=500)
  fieldOfProfessional=models.CharField(max_length=500)
  createdAt=models.DateTimeField(auto_now_add=True)
  updatedAt=models.DateTimeField(auto_now=True)

class ApplyJob(models.Model):
  firstName=models.CharField(max_length=500)
  lastName=models.CharField(max_length=500)
  email=models.EmailField()
  phoneNumber=models.CharField(max_length=250,blank=True)
  cvFile=models.FileField(upload_to='cv-files',editable=True)
  createdAt=models.DateTimeField(auto_now_add=True)
  updatedAt=models.DateTimeField(auto_now=True)
  
class Vacation(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  STATUS = ((1,'Pending'),(2,'Approved'),(3,'Decline'))
  status = models.IntegerField(choices=STATUS,default=1)
  uuid = models.UUIDField(default=uuid4, editable=False, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta:
        permissions = [
          ("can_create_mymodel", "Can create mymodel"),
          ("can_view_mymodel", "Can view mymodel"),
          ("can_edit_mymodel", "Can edit mymodel"),
          ("can_delete_mymodel", "Can delete mymodel"),
        ]
  
  
  
  def __str__(self):
    user = User.objects.get(id=self.user_id) 
    return user.first_name + " " + user.last_name
  
  



        


