from django.db import models

class Applicant(models.Model):

    SEMESTERS = (
        ('1', '1st'),
        ('2', '2nd'),
        ('3', '3rd'),
        ('4', '4th'),
        ('5', '5th'),
        ('6', '6th'))

    registered_at        = models.DateTimeField(auto_now_add=True)
    name                 = models.CharField(max_length=255)
    semester             = models.CharField(max_length=1, choices=SEMESTERS)
    exprienced_in_python = models.BooleanField(default=False)
    phone_number         = models.CharField(max_length=10, blank=True)
    email                = models.EmailField()
    solved_puzzle        = models.BooleanField(default=False)

    class Meta:
        ordering = ['name', 'semester']

    def __unicode__(self):
        return self.name
