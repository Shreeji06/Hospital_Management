from django.urls import path

from .views import DoctorListView,DoctorCreateView,DoctorDetailView,DoctorDeleteView,DoctorUpdateView
app_name  = 'doctor'
urlpatterns = [
    path('list/',DoctorListView,name='list'),
    path('create/',DoctorCreateView,name='create'),
    path('<int:pk>/detail/',DoctorDetailView,name='detail'),
    path('<int:pk>/delete/',DoctorDeleteView,name='delete'),
    path('<int:pk>/update/',DoctorUpdateView,name='update')
]