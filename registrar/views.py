from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .forms import ApplicantForm

def index(request):

    if request.method == 'GET':
        form = ApplicantForm()
        return render(request, 'registrar/index.html', {'form': form})
    elif request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            applicantObj = form.save()
            return render(request, 'registrar/index.html', {
                'form': ApplicantForm(),
                'applicant': applicantObj,
            })
        else:
            return render(request, 'registrar/index.html', {
                'form': ApplicantForm(request.POST),
            })



