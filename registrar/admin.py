from django.contrib import admin
from .models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
    fields = ('registered_at', 'name', 'semester', 'exprienced_in_python', 'phone_number', 'email')
    readonly_fields = ('registered_at',)
    list_display = ('name', 'semester', 'exprienced_in_python')
    list_filter = ('registered_at', 'semester')

admin.site.register(Applicant, ApplicantAdmin)
