# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'InsertPrice.start_price'
        db.alter_column('insert_price', 'start_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=4))

        # Changing field 'InsertPrice.price_per_insert'
        db.alter_column('insert_price', 'price_per_insert', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=4))

    def backwards(self, orm):

        # Changing field 'InsertPrice.start_price'
        db.alter_column('insert_price', 'start_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2))

        # Changing field 'InsertPrice.price_per_insert'
        db.alter_column('insert_price', 'price_per_insert', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2))

    models = {
        u'insert_price.insertprice': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'InsertPrice', 'db_table': "'insert_price'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_inserts_per_copy': ('django.db.models.fields.IntegerField', [], {}),
            'price_per_insert': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'})
        }
    }

    complete_apps = ['insert_price']