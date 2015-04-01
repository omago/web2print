# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Printer'
        db.create_table('printer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('color', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'printer', ['Printer'])


    def backwards(self, orm):
        # Deleting model 'Printer'
        db.delete_table('printer')


    models = {
        u'printer.printer': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Printer', 'db_table': "'printer'"},
            'color': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['printer']