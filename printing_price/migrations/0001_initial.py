# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PrintingPrice'
        db.create_table('printing_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('printer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['printer.Printer'])),
            ('quire_from', self.gf('django.db.models.fields.IntegerField')()),
            ('quire_to', self.gf('django.db.models.fields.IntegerField')()),
            ('start_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('click_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('both_sides_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
        ))
        db.send_create_signal(u'printing_price', ['PrintingPrice'])


    def backwards(self, orm):
        # Deleting model 'PrintingPrice'
        db.delete_table('printing_price')


    models = {
        u'printer.printer': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Printer', 'db_table': "'printer'"},
            'color': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        },
        u'printing_price.printingprice': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PrintingPrice', 'db_table': "'printing_price'"},
            'both_sides_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'click_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['printer.Printer']"}),
            'quire_from': ('django.db.models.fields.IntegerField', [], {}),
            'quire_to': ('django.db.models.fields.IntegerField', [], {}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'})
        }
    }

    complete_apps = ['printing_price']