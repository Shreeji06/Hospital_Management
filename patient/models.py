import datetime
from django.db import models
from django.utils import timezone
from doctor.models import Doctor

gender=[
    ('Male','Male'),
    ('Female','Female'),
    ('N/A','N/A')
]


marital_status=[('Single','Single'),
('Married','Married')
]



class Patient(models.Model):
    
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    date_of_Birth=models.DateField()
    email=models.EmailField(null=True)
    mobile = models.CharField(max_length=20)
    sex=models.CharField(max_length=20,choices=gender,default='Male')
    profile_pic=models.ImageField(null=True,blank=True)
    
    address=models.CharField(max_length=50)
    marital_status=models.CharField(max_length=20,choices=marital_status,default='single')
    emergency_contact=models.CharField(max_length=20)
    relationship=models.CharField(max_length=20)
    weight=models.CharField(max_length=20)
    height=models.CharField(max_length=20)
    other_medications_reason=models.CharField(max_length=100)
    symptoms=models.CharField(max_length=100)
    assignedDoctorId=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    admitDate=models.DateTimeField(default=datetime.datetime.today())
    status=models.BooleanField(default=False)
    

    def __str__(self):
        return f"{ self.first_name} | { self.symptoms}"


