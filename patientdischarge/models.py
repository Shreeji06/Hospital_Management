from re import M
from django.db import models
from patient.models import Patient
from doctor.models import Doctor
from datetime import datetime

class PatientDischargeDetails(models.Model):

    patientName=models.CharField(max_length=20)
    attending_physician=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date_service_end = models.DateField(null=True)
    room_type=models.CharField(max_length=30,null=True)
    assignedDoctorName=models.CharField(max_length=40)

    admitDate=models.DateTimeField()
    releaseDate=models.DateField(default=datetime.today())
    daySpent=models.PositiveIntegerField(null=False)


    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)
    paid=models.BooleanField(default=False)

    