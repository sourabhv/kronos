from django.contrib import admin
from .models import Applicant

class ApplicantAdmin(admin.ModelAdmin):
    fields = ('workshop', 'registered_at', 'name', 'year',
              'phone_number', 'email', 'solved_puzzle',)
    readonly_fields = ('registered_at',)
    list_display = ('workshop', 'name', 'year', 'solved_puzzle',)
    list_filter = ('workshop', 'registered_at', 'year', 'solved_puzzle',)

admin.site.register(Applicant, ApplicantAdmin)
