from django.shortcuts import render
from .forms import RequestForm

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
            form = RequestForm()
    
    else:
        form = RequestForm()
        
    form = RequestForm()
    template = 'forecast/forecast.html'
    context = {
    'form': form,
    }

    return render(request, template, context)
    
def requestSuccess(request):
    
    return render(request, 'forecast/success_request.html')