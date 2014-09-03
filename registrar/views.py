import os

from .codecha import Codecha
from django.shortcuts import render

from registrar.models import Applicant
from .forms import ApplicantForm


def index(request):
    """Renders the home page for contagious."""
    return render(request, 'registrar/index.html')


def register(request):
    """ Returns the registration page."""
    if request.method == 'GET':
        form = ApplicantForm()
        return render(request, 'registrar/register.html', {'form': form})

    elif request.method == 'POST':
            form = ApplicantForm(request.POST)

            # submit the form
            if form.is_valid():
                # set solved_puzzle to value from codecha_passed
                applicantObj = form.save(commit=False)
                applicantObj.solved_puzzle = codecha_passed(request)
                applicantObj.save()

                return render(request, 'registrar/register.html', {
                    'form': ApplicantForm(),
                    'applicant': applicantObj,
                })
            else:
                return render(request, 'registrar/register.html', {
                    'form': ApplicantForm(request.POST),
                })


def about(request):
    "Renders the about page"
    return render(request, 'registrar/about.html', {})

def home(request):
    "Renders the home page"
    return render(request,'registrar/home.html',{})

# Codecha code
def codecha_passed(request):
    "requests the codecha api for codecha challange status (failure/success)"
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
