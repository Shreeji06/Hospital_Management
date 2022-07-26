from django.urls import path

from .views import  DischargeCreateView,patientdishchargeListView,patientdishchargeDetailView,patientdishchargeDeleteView,patientdishchargeUpdateview
app_name  = 'discharge'
urlpatterns = [
    path('<int:pk>/create/',DischargeCreateView,name='create'),
    path('list/',patientdishchargeListView,name='list'),
    path('<int:pk>/detail/',patientdishchargeDetailView,name='detail'),
    path('<int:pk>/delete/',patientdishchargeDeleteView,name='delete'),
    path('<int:pk>/update/',patientdishchargeUpdateview,name='update')
]
