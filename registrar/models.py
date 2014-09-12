from django.db import models

from .workshops import WORKSHOPS

class Applicant(models.Model):

    SEMESTERS = (
        (u'1', u'1st Semester'),
        (u'2', u'2nd Semester'),
        (u'3', u'3rd Semester'),
        (u'4', u'4th Semester'),
        (u'5', u'5th Semester'),
        (u'6', u'6th Semester'),)

    EXPERIENCES = (
        (u'0', u'The snake? (None)'),
        (u'1', u'Heard once about it (Beginner)'),
        (u'2', u'I use it all the time (Experienced)'),
        (u'3', u'!! Pro Pythonista !!'),)

    registered_at     = models.DateTimeField(auto_now_add=True)
    workshop          = models.CharField(max_length=20, choices=WORKSHOPS)
    name              = models.CharField(max_length=255)
    semester          = models.CharField(max_length=1, choices=SEMESTERS)
    python_experience = models.CharField(max_length=1, choices=EXPERIENCES)
    phone_number      = models.CharField(max_length=10, blank=True)
    email             = models.EmailField()
    solved_puzzle     = models.BooleanField(default=False)

    class Meta:
        ordering = ['-solved_puzzle', 'registered_at', 'semester', 'name']

    def __unicode__(self):
        return self.name
