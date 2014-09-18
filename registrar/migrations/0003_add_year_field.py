# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        for applicant in orm.Applicant.objects.all():
            if applicant.semester in ['1', '2']:
                applicant.year = '1'
            elif applicant.semester in ['3', '4']:
                applicant.year = '2'
            elif applicant.semester == '5':
                applicant.year = '3'
            elif applicant.semester == '6':
                applicant.year = '4'
            applicant.save()

    def backwards(self, orm):
        "Write your backwards methods here."
        raise RuntimeError("Cannot reverse this migration")

    models = {
        u'registrar.applicant': {
            'Meta': {'ordering': "['-solved_puzzle', 'registered_at', 'semester', 'name']", 'object_name': 'Applicant'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'python_experience': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'registered_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'semester': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'solved_puzzle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'workshop': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'})
        }
    }

    complete_apps = ['registrar']
    symmetrical = True
