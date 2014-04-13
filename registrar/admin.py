from django.contrib import admin
from .models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
    fields = ('registered_at', 'name', 'semester', 'exprienced_in_python',
              'phone_number', 'email', 'solved_puzzle',)
    readonly_fields = ('registered_at',)
    list_display = ('name', 'semester', 'exprienced_in_python', 'solved_puzzle',)
    list_filter = ('registered_at', 'semester', 'solved_puzzle',)

admin.site.register(Applicant, ApplicantAdmin)
