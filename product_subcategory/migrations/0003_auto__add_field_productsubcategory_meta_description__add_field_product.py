# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ProductSubcategory.meta_description'
        db.add_column('product_subcategory', 'meta_description',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding field 'ProductSubcategory.meta_keywords'
        db.add_column('product_subcategory', 'meta_keywords',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ProductSubcategory.meta_description'
        db.delete_column('product_subcategory', 'meta_description')

        # Deleting field 'ProductSubcategory.meta_keywords'
        db.delete_column('product_subcategory', 'meta_keywords')


    models = {
        u'product_category.productcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ProductCategory', 'db_table': "'product_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        },
        u'product_subcategory.productsubcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ProductSubcategory', 'db_table': "'product_subcategory'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_category.ProductCategory']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['product_subcategory']