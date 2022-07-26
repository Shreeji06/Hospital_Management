from django.urls import path

from .views import AppointmentListView,AppointmentCreateView,AppointmentDetailView,AppointmentDeleteView,AppointmentUpdateview
app_name  = 'appointment'
urlpatterns = [
    path('list/',AppointmentListView,name='list'),
    path('<int:pk>/create/',AppointmentCreateView,name='create'),
    path('<int:pk>/detail/',AppointmentDetailView,name='detail'),
    path('<int:pk>/delete/',AppointmentDeleteView,name='delete'),
    path('<int:pk>/update/',AppointmentUpdateview,name='update')
]