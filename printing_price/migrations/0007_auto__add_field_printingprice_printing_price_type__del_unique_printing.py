# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'PrintingPrice', fields ['printer', 'both_sides', 'x']
        db.delete_unique('printing_price', ['printer_id', 'both_sides', 'x'])

        # Adding field 'PrintingPrice.printing_price_type'
        db.add_column('printing_price', 'printing_price_type',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=128),
                      keep_default=False)

        # Adding unique constraint on 'PrintingPrice', fields ['printer', 'both_sides', 'x', 'printing_price_type']
        db.create_unique('printing_price', ['printer_id', 'both_sides', 'x', 'printing_price_type'])


    def backwards(self, orm):
        # Removing unique constraint on 'PrintingPrice', fields ['printer', 'both_sides', 'x', 'printing_price_type']
        db.delete_unique('printing_price', ['printer_id', 'both_sides', 'x', 'printing_price_type'])

        # Deleting field 'PrintingPrice.printing_price_type'
        db.delete_column('printing_price', 'printing_price_type')

        # Adding unique constraint on 'PrintingPrice', fields ['printer', 'both_sides', 'x']
        db.create_unique('printing_price', ['printer_id', 'both_sides', 'x'])


    models = {
        u'press.press': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Press', 'db_table': "'press'"},
            'both_sides_print': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'printer.printer': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Printer', 'db_table': "'printer'"},
            'color': ('django.db.models.fields.BooleanField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'press': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'printer-press'", 'symmetrical': 'False', 'to': u"orm['press.Press']"}),
            'printing_price_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.BooleanField', [], {}),
            'user_discount': ('django.db.models.fields.BooleanField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'printing_price.printingprice': {
            'Meta': {'ordering': "['-pk']", 'unique_together': "(('printer', 'both_sides', 'x', 'printing_price_type'),)", 'object_name': 'PrintingPrice', 'db_table': "'printing_price'"},
            'both_sides': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['printer.Printer']"}),
            'printing_price_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'x_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'})
        }
    }

    complete_apps = ['printing_price']