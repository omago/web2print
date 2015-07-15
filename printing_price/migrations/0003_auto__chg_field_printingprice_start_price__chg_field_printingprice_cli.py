# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'PrintingPrice.start_price'
        db.alter_column('printing_price', 'start_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=4))

        # Changing field 'PrintingPrice.click_price'
        db.alter_column('printing_price', 'click_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=4))

    def backwards(self, orm):

        # Changing field 'PrintingPrice.start_price'
        db.alter_column('printing_price', 'start_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2))

        # Changing field 'PrintingPrice.click_price'
        db.alter_column('printing_price', 'click_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2))

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
            'click_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['printer.Printer']"}),
            'quire_from': ('django.db.models.fields.IntegerField', [], {}),
            'quire_to': ('django.db.models.fields.IntegerField', [], {}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'})
        }
    }

    complete_apps = ['printing_price']