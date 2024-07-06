from django.urls import path
from .views import AppointmentView, ManageAppointmentView

urlpatterns = [
    path("", AppointmentView.as_view(), name="appointment"),
    path("manage-appointments/", ManageAppointmentView.as_view(), name="manage"),
]