from django.urls import path
from .views import AppointmentView, ManageAppointmentView, DeleteAppointment


urlpatterns = [
    path("", AppointmentView.as_view(), name="appointment"),
    path("manage-appointments/",
         ManageAppointmentView.as_view(), name="manage"),
    path("<int:pk>/delete_appointment", DeleteAppointment.as_view(),
         name='delete_appointment')
]
