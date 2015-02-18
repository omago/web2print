# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.has_insert'
        db.alter_column('product', 'has_insert', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_rounding'
        db.alter_column('product', 'has_rounding', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_creasing'
        db.alter_column('product', 'has_creasing', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_improper_cutting'
        db.alter_column('product', 'has_improper_cutting', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_laminating'
        db.alter_column('product', 'has_laminating', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_mutations'
        db.alter_column('product', 'has_mutations', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_hole_drilling'
        db.alter_column('product', 'has_hole_drilling', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_plastic'
        db.alter_column('product', 'has_plastic', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_flexion'
        db.alter_column('product', 'has_flexion', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_vacuuming'
        db.alter_column('product', 'has_vacuuming', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_title'
        db.alter_column('product', 'has_title', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.cover'
        db.alter_column('product', 'cover', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_binding'
        db.alter_column('product', 'has_binding', self.gf('django.db.models.fields.BooleanField')(default=1))

        # Changing field 'Product.has_cutting'
        db.alter_column('product', 'has_cutting', self.gf('django.db.models.fields.BooleanField')(default=1))

    def backwards(self, orm):

        # Changing field 'Product.has_insert'
        db.alter_column('product', 'has_insert', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_rounding'
        db.alter_column('product', 'has_rounding', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_creasing'
        db.alter_column('product', 'has_creasing', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_improper_cutting'
        db.alter_column('product', 'has_improper_cutting', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_laminating'
        db.alter_column('product', 'has_laminating', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_mutations'
        db.alter_column('product', 'has_mutations', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_hole_drilling'
        db.alter_column('product', 'has_hole_drilling', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_plastic'
        db.alter_column('product', 'has_plastic', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_flexion'
        db.alter_column('product', 'has_flexion', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_vacuuming'
        db.alter_column('product', 'has_vacuuming', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_title'
        db.alter_column('product', 'has_title', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.cover'
        db.alter_column('product', 'cover', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_binding'
        db.alter_column('product', 'has_binding', self.gf('django.db.models.fields.NullBooleanField')(null=True))

        # Changing field 'Product.has_cutting'
        db.alter_column('product', 'has_cutting', self.gf('django.db.models.fields.NullBooleanField')(null=True))

    models = {
        u'binding.binding': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Binding', 'db_table': "'binding'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'flexion.flexion': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Flexion', 'db_table': "'flexion'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'paper.paper': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Paper', 'db_table': "'paper'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'plastic.plastic': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Plastic', 'db_table': "'plastic'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'press.press': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Press', 'db_table': "'press'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'product.product': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Product', 'db_table': "'product'"},
            'bindings': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['binding.Binding']", 'symmetrical': 'False'}),
            'cover': ('django.db.models.fields.BooleanField', [], {}),
            'cover_paper': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['paper.Paper']", 'symmetrical': 'False'}),
            'cover_plastic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plastic.Plastic']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'flexion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['flexion.Flexion']", 'symmetrical': 'False'}),
            'has_binding': ('django.db.models.fields.BooleanField', [], {}),
            'has_creasing': ('django.db.models.fields.BooleanField', [], {}),
            'has_cutting': ('django.db.models.fields.BooleanField', [], {}),
            'has_flexion': ('django.db.models.fields.BooleanField', [], {}),
            'has_hole_drilling': ('django.db.models.fields.BooleanField', [], {}),
            'has_improper_cutting': ('django.db.models.fields.BooleanField', [], {}),
            'has_insert': ('django.db.models.fields.BooleanField', [], {}),
            'has_laminating': ('django.db.models.fields.BooleanField', [], {}),
            'has_mutations': ('django.db.models.fields.BooleanField', [], {}),
            'has_plastic': ('django.db.models.fields.BooleanField', [], {}),
            'has_rounding': ('django.db.models.fields.BooleanField', [], {}),
            'has_title': ('django.db.models.fields.BooleanField', [], {}),
            'has_vacuuming': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'insert_paper': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'insert_paper'", 'symmetrical': 'False', 'to': u"orm['paper.Paper']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'paper': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'paper'", 'symmetrical': 'False', 'to': u"orm['paper.Paper']"}),
            'plastic': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'plastic'", 'symmetrical': 'False', 'to': u"orm['plastic.Plastic']"}),
            'press': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['press.Press']", 'symmetrical': 'False'}),
            'product_formats': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['product_format.ProductFormat']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_subcategory.ProductSubcategory']"})
        },
        u'product_category.productcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ProductCategory', 'db_table': "'product_category'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        },
        u'product_format.productformat': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ProductFormat', 'db_table': "'product_format'"},
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'product_subcategory.productsubcategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ProductSubcategory', 'db_table': "'product_subcategory'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_category.ProductCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['product']