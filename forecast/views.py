from django.shortcuts import render
from .forms import RequestForm
from django.contrib import messages

# Create your views here.


def requestHelp(request):
    """
    View for processing the submission of the request form
    """
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'forecast/success_request.html')
        else:
            messages.error(request, 'Please ensure the form is valid'
                                    ' or you haven´t filled in the field.')
    else:
        form = RequestForm()

    return render(request, 'forecast/forecast.html', {'form': form})


def requestSuccess(request):

    return render(request, 'forecast/success_request.html')