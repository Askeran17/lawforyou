from django.http.response import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView
from django.template.loader import get_template
from django.contrib.messages.views import SuccessMessageMixin


class AppointmentView(TemplateView):
    '''view for booking appointment'''
    template_name = "appointment/appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        appointment = Appointment.objects.create(
            first_name=fname,
            last_name=lname,
            email=email,
            phone=phone,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment, we will email you soon!")  # noqa
        return HttpResponseRedirect(request.path)


class ManageAppointmentView(ListView):
    '''view for manage appointments'''
    queryset = Appointment.objects.all().order_by("-sent_date", "-id")
    template_name = "appointment/manage-appointment.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 6

    def post(self, request):
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.appointment_date = date
        appointment.accepted = True
        appointment.save()

        data = {
            "fname": appointment.first_name,
            "date": appointment.appointment_date,
        }

        message = get_template('appointment/email.html').render(data)
        email = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
        )
        email.content_subtype = "html"
        email.send()

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {appointment.first_name}")  # noqa
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        appointments = Appointment.objects.all()
        context.update({
            "title": "Manage Appointments"
        })
        return context


class DeleteAppointment(SuccessMessageMixin, DeleteView):
    '''admin can delete appointment from the website itself'''
    model = Appointment
    template_name = 'appointment/delete_appointment.html'
    success_url = reverse_lazy('manage')
    success_message = "Appointment deleted!"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(DeleteAppointment, self).delete(request, *args, **kwargs)
