# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Printer.click_width'
        db.add_column('printer', 'click_width',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Printer.click_width'
        db.delete_column('printer', 'click_width')


    models = {
        u'press.press': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Press', 'db_table': "'press'"},
            'both_sides_print': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'printer.printer': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Printer', 'db_table': "'printer'"},
            'click_width': ('django.db.models.fields.IntegerField', [], {}),
            'color': ('django.db.models.fields.BooleanField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'press': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'printer-press'", 'symmetrical': 'False', 'to': u"orm['press.Press']"}),
            'printing_price_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.BooleanField', [], {}),
            'user_discount': ('django.db.models.fields.BooleanField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['printer']