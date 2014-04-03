from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ApplicantForm

def index(request):
    form = ApplicantForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/thanks')

    return render(request, 'registrar/index.html', {
        'form': form
        })

def thanks(request):
    return render(request, 'registrar/thanks.html', {})
