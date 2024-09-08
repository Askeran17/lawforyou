from django.urls import path
from .views import AppointmentView, ManageAppointmentView, DeleteAppointment
from . import views

urlpatterns = [
    path("", AppointmentView.as_view(), name="appointment"),
    path("manage-appointments/",
         ManageAppointmentView.as_view(), name="manage"),
    path("<int:pk>/delete_appointment", views.DeleteAppointment.as_view(),
         name='delete_appointment')
]