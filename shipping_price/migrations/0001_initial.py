# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShippingPrice'
        db.create_table('shipping_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight_from', self.gf('django.db.models.fields.IntegerField')()),
            ('weight_to', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=4)),
        ))
        db.send_create_signal(u'shipping_price', ['ShippingPrice'])

        # Adding unique constraint on 'ShippingPrice', fields ['weight_from', 'weight_to']
        db.create_unique('shipping_price', ['weight_from', 'weight_to'])


    def backwards(self, orm):
        # Removing unique constraint on 'ShippingPrice', fields ['weight_from', 'weight_to']
        db.delete_unique('shipping_price', ['weight_from', 'weight_to'])

        # Deleting model 'ShippingPrice'
        db.delete_table('shipping_price')


    models = {
        u'shipping_price.shippingprice': {
            'Meta': {'ordering': "['-pk']", 'unique_together': "(('weight_from', 'weight_to'),)", 'object_name': 'ShippingPrice', 'db_table': "'shipping_price'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            'weight_from': ('django.db.models.fields.IntegerField', [], {}),
            'weight_to': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['shipping_price']