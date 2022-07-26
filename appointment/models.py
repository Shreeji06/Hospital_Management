from django.db import models

class Appointment(models.Model):
    patientName=models.CharField(max_length=20)
    doctorName=models.CharField(max_length=20)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)

    
    