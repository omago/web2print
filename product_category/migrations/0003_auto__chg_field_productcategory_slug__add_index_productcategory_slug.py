# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ProductCategory.slug'
        db.alter_column('product_category', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=128))
        # Adding index on 'ProductCategory', fields ['slug']
        db.create_index('product_category', ['slug'])


    def backwards(self, orm):
        # Removing index on 'ProductCategory', fields ['slug']
        db.delete_index('product_category', ['slug'])


        # Changing field 'ProductCategory.slug'
        db.alter_column('product_category', 'slug', self.gf('django.db.models.fields.CharField')(max_length=128))

    models = {
        u'product_category.productcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ProductCategory', 'db_table': "'product_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['product_category']