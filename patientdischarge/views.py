from dataclasses import dataclass
from django.shortcuts import render,redirect
from patient.models import Patient
from .models import PatientDischargeDetails
from doctor.models import Doctor
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.


def DischargeCreateView(request, pk):

    if request.method == 'GET':
        date = datetime.now()
        old_patient = Patient.objects.get(pk=pk)
        patient = Patient(pk=pk)
        patient.first_name = old_patient.first_name
        patient.last_name = old_patient.last_name        
        patient.date_of_Birth = old_patient.date_of_Birth
        patient.email = old_patient.email
        patient.mobile = old_patient.mobile
        patient.sex = old_patient.sex
        patient.profile_pic = old_patient.profile_pic
        patient.address = old_patient.address
        patient.marital_status = old_patient.marital_status
        patient.emergency_contact = old_patient.emergency_contact
        patient.relationship = old_patient.relationship
        patient.weight = old_patient.weight
        patient.height = old_patient.height
        patient.other_medications_reason = old_patient.other_medications_reason
        patient.symptoms = old_patient.symptoms
        patient.assignedDoctorId_id =old_patient.assignedDoctorId_id
        patient.admitDate = old_patient.admitDate
        patient.status = '1'
        patient.save()
        pat = Patient.objects.get(pk=pk)
        doctor = Doctor.objects.all()
        return render(request,'patientdischarge/discharge_create.html',{'patient':pat,'doctor':doctor,'date':date})



        #  It will  add new patientdishcharge.


    if request.method == 'POST':

        context = request.POST
        patient=PatientDischargeDetails(pk=pk)

        patient.patientName = context['p_name']
        patient.attending_physician_id = context['ap']
        patient.date_service_end = context['e_date']
        patient.room_type = context['room']
        patient.assignedDoctorName = context['ad_name']
        
        pat = Patient.objects.get(pk=pk)
        date = pat.admitDate
        patient.admitDate = date
        a_date = datetime.date(date)
        r_date = datetime.now().date()
        
        def day_count(d1, d2):
            delta = d2 - d1
            return delta.days       
        
        patient.daySpent = day_count(a_date, r_date)
        patient.roomCharge = context['r_charge']
        patient.medicineCost = context['m_cost']
        patient.doctorFee = context['d_cost']
        patient.OtherCharge = context['o_cost'] 

        def total_cost(r_charge, m_charge, d_fees, o_charge):
            return int(r_charge) + int(m_charge) + int(d_fees) + int(o_charge)

        patient.total = total_cost(context['r_charge'],context['m_cost'],context['d_cost'], context['o_cost'] )
        
        if 'paid' in context:
            patient.paid = 'True'
        else:
            patient.paid = 'False'

        patient.save()
        return redirect('discharge:list')



# It will show the list of patientdishcharge.
def patientdishchargeListView(request):
    
    if request.method == 'GET':
       
        patients=PatientDischargeDetails.objects.all()
        return render(request,'patientdischarge/discharge_list.html',{'patients':patients})    


# It will show the detail of patientdishcharge

def patientdishchargeDetailView(request,pk):

    if request.method == 'GET':
        pat_detail=PatientDischargeDetails.objects.get(pk=pk)
        return render(request,'patientdischarge/discharge_detail.html',{'pat_detail':pat_detail})   



# It will delete the patient

def patientdishchargeDeleteView(request,pk):

    if request.method == 'GET':
        delete_record=PatientDischargeDetails(pk=pk)
        delete_record.delete()


    return redirect('discharge:list')     



#  It will update the detail of patient discharge

def patientdishchargeUpdateview(request,pk):

    if request.method == 'GET':
        pat=PatientDischargeDetails.objects.get(pk=pk)
        patient=Patient.objects.all()
        doctor=Doctor.objects.all()
        return render(request,'patientdischarge/discharge_update.html',{'pat':pat,'patient':patient,'doctor':doctor})


    if request.method == 'POST':

       if request.method == 'POST':

        context = request.POST
        patient=PatientDischargeDetails(pk=pk)

        patient.patientName = context['p_name']
        patient.attending_physician_id = context['ap']
        patient.date_service_end = context['e_date']
        patient.room_type = context['room']
        patient.assignedDoctorName = context['ad_name']
        
        pat = Patient.objects.get(pk=pk)
        date = pat.admitDate
        patient.admitDate = date
        a_date = datetime.date(date)
        r_date = datetime.now().date()
        
        def day_count(d1, d2):
            delta = d2 - d1
            return delta.days       
        
        patient.daySpent = day_count(a_date, r_date)
        patient.roomCharge = context['r_charge']
        patient.medicineCost = context['m_cost']
        patient.doctorFee = context['d_cost']
        patient.OtherCharge = context['o_cost'] 

        def total_cost(r_charge, m_charge, d_fees, o_charge):
            return int(r_charge) + int(m_charge) + int(d_fees) + int(o_charge)

        patient.total = total_cost(context['r_charge'],context['m_cost'],context['d_cost'], context['o_cost'] )
        

        patient.save()
        return redirect('discharge:list')




