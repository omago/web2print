# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Printer.width'
        db.add_column('printer', 'width',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Printer.height'
        db.add_column('printer', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Printer.width'
        db.delete_column('printer', 'width')

        # Deleting field 'Printer.height'
        db.delete_column('printer', 'height')


    models = {
        u'printer.printer': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Printer', 'db_table': "'printer'"},
            'color': ('django.db.models.fields.BooleanField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['printer']