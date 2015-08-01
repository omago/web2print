# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'InsertPrice', fields ['start_price', 'number_of_inserts_per_copy', 'price_per_insert']
        db.create_unique('insert_price', ['start_price', 'number_of_inserts_per_copy', 'price_per_insert'])


    def backwards(self, orm):
        # Removing unique constraint on 'InsertPrice', fields ['start_price', 'number_of_inserts_per_copy', 'price_per_insert']
        db.delete_unique('insert_price', ['start_price', 'number_of_inserts_per_copy', 'price_per_insert'])


    models = {
        u'insert_price.insertprice': {
            'Meta': {'ordering': "['-pk']", 'unique_together': "(('start_price', 'number_of_inserts_per_copy', 'price_per_insert'),)", 'object_name': 'InsertPrice', 'db_table': "'insert_price'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_inserts_per_copy': ('django.db.models.fields.IntegerField', [], {}),
            'price_per_insert': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'})
        }
    }

    complete_apps = ['insert_price']