from django.urls import path

from .views import PatientListView,PatientCreateView,PatientDetailView,PatientDeleteView,PatientUpdateview
app_name  = 'patient'
urlpatterns = [
    path('list/',PatientListView,name='list'),
    path('create/',PatientCreateView,name='create'),
    path('<int:pk>/detail/',PatientDetailView,name='detail'),
    path('<int:pk>/delete/',PatientDeleteView,name='delete'),
    path('<int:pk>/update/',PatientUpdateview,name='update')
]