# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductFormat'
        db.create_table('product_format', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('height', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'product_format', ['ProductFormat'])


    def backwards(self, orm):
        # Deleting model 'ProductFormat'
        db.delete_table('product_format')


    models = {
        u'product_format.ProductFormat': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ProductFormat', 'db_table': "'product_format'"},
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['product_format']