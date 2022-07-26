from django.shortcuts import render,redirect
from .models import Doctor
from django.contrib.auth.decorators import login_required


#It will show list the info of doctors
@login_required
def DoctorListView(request):

    if request.method == 'GET':
        docs = Doctor.objects.all()
        return render(request, 'doctor/doctor_list.html',{'docs':docs})

#For Creation of new doctor
@login_required
def DoctorCreateView(request):

    #Return registration form
    if request.method == 'GET':
        return render(request, 'doctor/doctor_create.html')

    #Add new doctor and redirect to list-page
    if request.method == 'POST':

        context = request.POST

        doctor = Doctor()
        doctor.first_name = context['fname']
        doctor.last_name = context['lname']
        doctor.profile_pic = context['pic']
        doctor.email = context['email']
        doctor.address = context['address']
        doctor.mobile = context['mobile']
        doctor.marital_status = context['m_status']
        doctor.sex = context['sex']
        doctor.department = context['department']
        if 'status' in context:
            doctor.status = 'True'
        else:
            doctor.status = 'False'
        
        
        doctor.save()
        return redirect('doctor:list')


# Show the detail of the individual doctor using ID
@login_required
def DoctorDetailView(request, pk):

    if request.method == 'GET':
        doc_detail = Doctor.objects.get(pk=pk)
        return render(request, 'doctor/doctor_detail.html', {'doc_detail':doc_detail})

#Delete the doctor 
@login_required
def DoctorDeleteView(request, pk):
    
    if request.method == 'GET':
        delete_record = Doctor(pk=pk)
        delete_record.delete()

    return redirect('doctor:list')

#Update the info of the doctor    
@login_required    
def DoctorUpdateView(request,pk):

    #Return the registration form
    if request.method == 'GET':
        doc= Doctor.objects.get(pk=pk)
        return render(request, 'doctor/Doctor_update.html',{'doc':doc})


    #Save the updated info and show updated detail of the doctor
    if request.method == 'POST':

        context= request.POST
        doc_detail = Doctor(pk=pk)

        doc_detail.first_name = context['fname']
        doc_detail.last_name = context['lname']
        doc_detail.profile_pic = context['pic']
        doc_detail.email = context['email']
        doc_detail.address = context['address']
        doc_detail.mobile = context['mobile']
        doc_detail.marital_status = context['m_status']
        doc_detail.sex = context['sex']
        doc_detail.department = context['depart']
        if 'status' in context:
                doc_detail.status = 'True'
        else:
                doc_detail.status = 'False'
        doc_detail.save()  
        return redirect('doctor:list')

