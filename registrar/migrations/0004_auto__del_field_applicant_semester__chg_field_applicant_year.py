# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Applicant.semester'
        db.delete_column(u'registrar_applicant', 'semester')


        # Changing field 'Applicant.year'
        db.alter_column(u'registrar_applicant', 'year', self.gf('django.db.models.fields.CharField')(max_length=1))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Applicant.semester'
        raise RuntimeError("Cannot reverse this migration. 'Applicant.semester' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Applicant.semester'
        db.add_column(u'registrar_applicant', 'semester',
                      self.gf('django.db.models.fields.CharField')(max_length=1),
                      keep_default=False)


        # Changing field 'Applicant.year'
        db.alter_column(u'registrar_applicant', 'year', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

    models = {
        u'registrar.applicant': {
            'Meta': {'ordering': "['-solved_puzzle', 'registered_at', 'year', 'name']", 'object_name': 'Applicant'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'python_experience': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'registered_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'solved_puzzle': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'workshop': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'year': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'})
        }
    }

    complete_apps = ['registrar']