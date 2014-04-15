from django.db import models

class Applicant(models.Model):

    SEMESTERS = (
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
        ('3', '3rd Semester'),
        ('4', '4th Semester'),
        ('5', '5th Semester'),
        ('6', '6th Semester'))

    EXPERIENCES = (
        ('0', 'The snake? (None)'),
        ('1', 'Heard once about it (Beginner)'),
        ('2', 'I use it all the time (Experienced)'),
        ('3', '!! Pro Pythonista !!'))

    registered_at        = models.DateTimeField(auto_now_add=True)
    name                 = models.CharField(max_length=255)
    semester             = models.CharField(max_length=1, choices=SEMESTERS)
    python_exprience     = models.CharField(max_length=1, choices=EXPERIENCES)
    phone_number         = models.CharField(max_length=10, blank=True)
    email                = models.EmailField()
    solved_puzzle        = models.BooleanField(default=False)

    class Meta:
        ordering = ['-solved_puzzle', 'registered_at', 'name', 'semester']

    def __unicode__(self):
        return self.name
