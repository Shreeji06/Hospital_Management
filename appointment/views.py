from django.shortcuts import render,redirect
from. models import Appointment
from patient.models import Patient
from django.contrib.auth.decorators import login_required


# It will show the list of Appointments.
@login_required
def AppointmentListView(request):
    
    if request.method == 'GET':
        appointments=Appointment.objects.all()
        return render(request,'appointment/appointment_list.html',{'appointments':appointments})


#  It will  add new appointment.
@login_required
def AppointmentCreateView(request, pk):

    if request.method == 'GET':
        patient = Patient.objects.get(pk=pk)
        return render(request,'appointment/appointment_create.html',{'patient':patient})


    if request.method == 'POST':

        context = request.POST
        appointment=Appointment()

        appointment.patientName = context['p_id']
        appointment.doctorName = context['d_id']        
        
        appointment.appointmentDate = context['a_date']
        appointment.description = context['description']
        if 'status' in context:
            appointment.status = 'True'
        else:
            appointment.status = 'False'
        

        appointment.save()
        return redirect('appointment:list')


# It will show the detail of particular appointments
@login_required
def AppointmentDetailView(request,pk):

    if request.method == 'GET':
        app_detail=Appointment.objects.get(pk=pk)
        return render(request,'appointment/appointment_detail.html',{'app_detail':app_detail})


# It will delete the appointment
@login_required
def AppointmentDeleteView(request,pk):

    if request.method == 'GET':
        delete_record=Appointment(pk=pk)
        delete_record.delete()


    return redirect('appointment:list')     


#  It will update the detail of appointment
@login_required
def AppointmentUpdateview(request,pk):

    if request.method == 'GET':
        appointment=Appointment.objects.get(pk=pk)
        return render(request,'appointment/appointment_update.html',{'appointment':appointment})


    if request.method == 'POST':

        context=request.POST
        appointment=Appointment(pk=pk)
        appointment.patientName = context['p_id']
        appointment.doctorName = context['d_id']        
        appointment.appointmentDate = context['a_date']
        appointment.description = context['description']
        if 'status' in context:
            appointment.status = 'True'
        else:
            appointment.status = 'False'
        
        appointment.save()
        return redirect('appointment:list')


