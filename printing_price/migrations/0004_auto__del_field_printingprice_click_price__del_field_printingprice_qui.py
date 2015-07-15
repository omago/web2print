# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PrintingPrice.click_price'
        db.delete_column('printing_price', 'click_price')

        # Deleting field 'PrintingPrice.quire_to'
        db.delete_column('printing_price', 'quire_to')

        # Deleting field 'PrintingPrice.quire_from'
        db.delete_column('printing_price', 'quire_from')

        # Adding field 'PrintingPrice.x'
        db.add_column('printing_price', 'x',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Adding field 'PrintingPrice.x_price'
        db.add_column('printing_price', 'x_price',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=11, decimal_places=4),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'PrintingPrice.click_price'
        db.add_column('printing_price', 'click_price',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=11, decimal_places=4),
                      keep_default=False)

        # Adding field 'PrintingPrice.quire_to'
        db.add_column('printing_price', 'quire_to',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Adding field 'PrintingPrice.quire_from'
        db.add_column('printing_price', 'quire_from',
                      self.gf('django.db.models.fields.IntegerField')(default=None),
                      keep_default=False)

        # Deleting field 'PrintingPrice.x'
        db.delete_column('printing_price', 'x')

        # Deleting field 'PrintingPrice.x_price'
        db.delete_column('printing_price', 'x_price')


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
            'role': ('django.db.models.fields.BooleanField', [], {}),
            'user_discount': ('django.db.models.fields.BooleanField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'printing_price.printingprice': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PrintingPrice', 'db_table': "'printing_price'"},
            'both_sides': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['printer.Printer']"}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'x_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'})
        }
    }

    complete_apps = ['printing_price']