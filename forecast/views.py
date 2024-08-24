from django.shortcuts import render
from .forms import RequestForm
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def forecast(request):
    return render(request, 'forecast/forecast.html')

def request_help(request):

    """
    View to handle contact form submission
    """
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your message has been sent!')
            return HttpResponseRedirect('forecast/forecast.html')

        else:
            form = RequestForm()
            messages.warning(request, 'Fail, your message is not sent. Please try again.')

    else:
        form = RequestForm()
        if 'submitted' in request.GET:
            form = ContactForm()
 
    form = RequestForm()
    template = 'forecast/forecast.html'
    context = {
        'form': form,
    }

    return render(request, template, context)