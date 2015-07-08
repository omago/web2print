# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PrintingPrice.both_sides_price'
        db.delete_column('printing_price', 'both_sides_price')

        # Adding field 'PrintingPrice.both_sides'
        db.add_column('printing_price', 'both_sides',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PrintingPrice.both_sides_price'
        db.add_column('printing_price', 'both_sides_price',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=11, decimal_places=2),
                      keep_default=False)

        # Deleting field 'PrintingPrice.both_sides'
        db.delete_column('printing_price', 'both_sides')


    models = {
        u'printer.printer': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Printer', 'db_table': "'printer'"},
            'color': ('django.db.models.fields.BooleanField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'printing_price.printingprice': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PrintingPrice', 'db_table': "'printing_price'"},
            'both_sides': ('django.db.models.fields.BooleanField', [], {}),
            'click_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['printer.Printer']"}),
            'quire_from': ('django.db.models.fields.IntegerField', [], {}),
            'quire_to': ('django.db.models.fields.IntegerField', [], {}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'})
        }
    }

    complete_apps = ['printing_price']