# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Printer.height'
        db.delete_column('printer', 'height')

        # Deleting field 'Printer.width'
        db.delete_column('printer', 'width')

        # Adding field 'Printer.printing_area_width'
        db.add_column('printer', 'printing_area_width',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Printer.printing_area_height'
        db.add_column('printer', 'printing_area_height',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Printer.max_paper_width'
        db.add_column('printer', 'max_paper_width',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Printer.max_paper_height'
        db.add_column('printer', 'max_paper_height',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Printer.height'
        db.add_column('printer', 'height',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Adding field 'Printer.width'
        db.add_column('printer', 'width',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Deleting field 'Printer.printing_area_width'
        db.delete_column('printer', 'printing_area_width')

        # Deleting field 'Printer.printing_area_height'
        db.delete_column('printer', 'printing_area_height')

        # Deleting field 'Printer.max_paper_width'
        db.delete_column('printer', 'max_paper_width')

        # Deleting field 'Printer.max_paper_height'
        db.delete_column('printer', 'max_paper_height')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_paper_height': ('django.db.models.fields.IntegerField', [], {}),
            'max_paper_width': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'paper_weight_payment_threshold': ('django.db.models.fields.IntegerField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'press': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'printer-press'", 'symmetrical': 'False', 'to': u"orm['press.Press']"}),
            'printing_area_height': ('django.db.models.fields.IntegerField', [], {}),
            'printing_area_width': ('django.db.models.fields.IntegerField', [], {}),
            'printing_price_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.BooleanField', [], {}),
            'user_discount': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['printer']