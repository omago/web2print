# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'InsertPrice'
        db.create_table('insert_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('number_of_inserts_per_copy', self.gf('django.db.models.fields.IntegerField')()),
            ('price_per_insert', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
        ))
        db.send_create_signal(u'insert_price', ['InsertPrice'])


    def backwards(self, orm):
        # Deleting model 'InsertPrice'
        db.delete_table('insert_price')


    models = {
        u'insert_price.insertprice': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'InsertPrice', 'db_table': "'insert_price'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_inserts_per_copy': ('django.db.models.fields.IntegerField', [], {}),
            'price_per_insert': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'})
        }
    }

    complete_apps = ['insert_price']