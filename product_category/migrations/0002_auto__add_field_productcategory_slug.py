# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProductCategory.slug'
        db.add_column('product_category', 'slug',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=128),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProductCategory.slug'
        db.delete_column('product_category', 'slug')


    models = {
        u'product_category.productcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ProductCategory', 'db_table': "'product_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['product_category']