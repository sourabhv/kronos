import os

from .codecha import Codecha
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from .forms import ApplicantForm

def codecha_passed(request):
    codecha_challenge = request.POST.get('codecha_challenge_field', False)
    codecha_response  = request.POST.get('codecha_response_field', False)

    codecha_key   = os.environ.get('CODECHAKEY')

    ip = __get_ip(request)

    if codecha_challenge and codecha_response:
        codecha_success = Codecha.verify(codecha_challenge, codecha_response, ip, codecha_key)
    else:
        codecha_success = False

    if codecha_success:
        return True
    else:
        return False

def __get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip

def index(request):

    if request.method == 'GET':
        form = ApplicantForm()
        return render(request, 'registrar/index.html', {'form': form})
    elif request.method == 'POST':
            form = ApplicantForm(request.POST)
            if form.is_valid() and codecha_passed(request):
                applicantObj = form.save()
                return render(request, 'registrar/index.html', {
                    'form': ApplicantForm(),
                    'applicant': applicantObj,
                })
            else:
                return render(request, 'registrar/index.html', {
                    'form': ApplicantForm(request.POST),
                })
