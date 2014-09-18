# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Applicant'
        db.create_table(u'registrar_applicant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registered_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('workshop', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('semester', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('python_experience', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('solved_puzzle', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'registrar', ['Applicant'])


    def backwards(self, orm):
        # Deleting model 'Applicant'
        db.delete_table(u'registrar_applicant')


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
            'workshop': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['registrar']