from django.shortcuts import render,redirect

from appointment.models import Appointment
from. models import Patient
from doctor.models import Doctor
from django.contrib.auth.decorators import login_required


# It will show the list of patient.
@login_required
def PatientListView(request):
    
    if request.method == 'GET':
        patients=Patient.objects.all()
        return render(request,'patient/patient_list.html',{'patients':patients})


#  It will  add new patient.
@login_required
def PatientCreateView(request):

    if request.method == 'GET':
        docs = Doctor.objects.all()
   
        return render(request,'patient/patient_create.html',{'docs':docs})


    if request.method == 'POST':

        context = request.POST
        print(context)
        patient=Patient()

        patient.first_name = context['fname']
        patient.last_name = context['lname']        
        patient.date_of_Birth = context['dob']
        patient.email = context['email']
        patient.mobile = context['mobile']
        patient.sex = context['sex']
        patient.profile_pic = context['pic']
        patient.address = context['add']
        patient.marital_status = context['m_status']
        patient.emergency_contact = context['e_contact']
        patient.relationship = context['relation']
        patient.weight = context['weight']
        patient.height = context['height']
        patient.other_medications_reason = context['reason']
        patient.symptoms = context['symptons']
        patient.assignedDoctorId_id =context['d_id']
        # patient.admitDate = context['a_date']
        if 'status' in context:
            patient.status = 'True'
        else:
            patient.status = 'False'
        

        patient.save()
        return redirect('patient:list')


# It will show the detail of particular patient
@login_required
def PatientDetailView(request,pk):

    if request.method == 'GET':
        pat_detail=Patient.objects.get(pk=pk)
        return render(request,'patient/patient_detail.html',{'pat_detail':pat_detail})


# It will delete the patient
@login_required
def PatientDeleteView(request,pk):

    if request.method == 'GET':
        delete_record=Patient(pk=pk)
        delete_record.delete()


    return redirect('patient:list')     


#  It will update the detail of patient
@login_required
def PatientUpdateview(request,pk):

    if request.method == 'GET':
        pat=Patient.objects.get(pk=pk)
        docs = Doctor.objects.all()
        return render(request,'patient/patient_update.html',{'pat':pat,'docs':docs})


    if request.method == 'POST':

        context=request.POST
        patient=Patient(pk=pk)
        patient.first_name = context['fname']
        patient.last_name = context['lname']        
        patient.date_of_Birth = context['dob']
        patient.email = context['email']
        patient.mobile = context['mobile']
        patient.sex = context['sex']
        patient.profile_pic = context['pic']
        patient.address = context['add']
        patient.marital_status = context['m_status']
        patient.emergency_contact = context['e_contact']
        patient.relationship = context['relation']
        patient.weight = context['weight']
        patient.height = context['height']
        patient.other_medications_reason = context['reason']
        patient.symptoms = context['symptoms']
        patient.assignedDoctorId_id = context['d_id'] 
        # patient.admitDate = context['a_date']
        if 'status' in context:
            patient.status = 'True'
        else:
            patient.status = 'False'
        
        patient.save()
        return redirect('patient:list')


