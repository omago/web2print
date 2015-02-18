# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.has_title'
        db.add_column('product', 'has_title',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_mutations'
        db.add_column('product', 'has_mutations',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.cover'
        db.add_column('product', 'cover',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_insert'
        db.add_column('product', 'has_insert',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_cutting'
        db.add_column('product', 'has_cutting',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_improper_cutting'
        db.add_column('product', 'has_improper_cutting',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_creasing'
        db.add_column('product', 'has_creasing',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_hole_drilling'
        db.add_column('product', 'has_hole_drilling',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_vacuuming'
        db.add_column('product', 'has_vacuuming',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_binding'
        db.add_column('product', 'has_binding',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_flexion'
        db.add_column('product', 'has_flexion',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_laminating'
        db.add_column('product', 'has_laminating',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_plastic'
        db.add_column('product', 'has_plastic',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Product.has_rounding'
        db.add_column('product', 'has_rounding',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field product_formats on 'Product'
        m2m_table_name = db.shorten_name('product_product_formats')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'product.product'], null=False)),
            ('productformat', models.ForeignKey(orm[u'product_format.productformat'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'productformat_id'])

        # Adding M2M table for field paper on 'Product'
        m2m_table_name = db.shorten_name('product_paper')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'product.product'], null=False)),
            ('paper', models.ForeignKey(orm[u'paper.paper'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'paper_id'])

        # Adding M2M table for field press on 'Product'
        m2m_table_name = db.shorten_name('product_press')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'product.product'], null=False)),
            ('press', models.ForeignKey(orm[u'press.press'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'press_id'])

        # Adding M2M table for field cover_paper on 'Product'
        m2m_table_name = db.shorten_name('product_cover_paper')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'product.product'], null=False)),
            ('paper', models.ForeignKey(orm[u'paper.paper'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'paper_id'])

        # Adding M2M table for field cover_plastic on 'Product'
        m2m_table_name = db.shorten_name('product_cover_plastic')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'product.product'], null=False)),
            ('plastic', models.ForeignKey(orm[u'plastic.plastic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'plastic_id'])

        # Adding M2M table for field insert_paper on 'Product'
        m2m_table_name = db.shorten_name('product_insert_paper')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'product.product'], null=False)),
            ('paper', models.ForeignKey(orm[u'paper.paper'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'paper_id'])

        # Adding M2M table for field bindings on 'Product'
        m2m_table_name = db.shorten_name('product_bindings')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'product.product'], null=False)),
            ('binding', models.ForeignKey(orm[u'binding.binding'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'binding_id'])

        # Adding M2M table for field flexion on 'Product'
        m2m_table_name = db.shorten_name('product_flexion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'product.product'], null=False)),
            ('flexion', models.ForeignKey(orm[u'flexion.flexion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'flexion_id'])

        # Adding M2M table for field plastic on 'Product'
        m2m_table_name = db.shorten_name('product_plastic')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'product.product'], null=False)),
            ('plastic', models.ForeignKey(orm[u'plastic.plastic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'plastic_id'])


    def backwards(self, orm):
        # Deleting field 'Product.has_title'
        db.delete_column('product', 'has_title')

        # Deleting field 'Product.has_mutations'
        db.delete_column('product', 'has_mutations')

        # Deleting field 'Product.cover'
        db.delete_column('product', 'cover')

        # Deleting field 'Product.has_insert'
        db.delete_column('product', 'has_insert')

        # Deleting field 'Product.has_cutting'
        db.delete_column('product', 'has_cutting')

        # Deleting field 'Product.has_improper_cutting'
        db.delete_column('product', 'has_improper_cutting')

        # Deleting field 'Product.has_creasing'
        db.delete_column('product', 'has_creasing')

        # Deleting field 'Product.has_hole_drilling'
        db.delete_column('product', 'has_hole_drilling')

        # Deleting field 'Product.has_vacuuming'
        db.delete_column('product', 'has_vacuuming')

        # Deleting field 'Product.has_binding'
        db.delete_column('product', 'has_binding')

        # Deleting field 'Product.has_flexion'
        db.delete_column('product', 'has_flexion')

        # Deleting field 'Product.has_laminating'
        db.delete_column('product', 'has_laminating')

        # Deleting field 'Product.has_plastic'
        db.delete_column('product', 'has_plastic')

        # Deleting field 'Product.has_rounding'
        db.delete_column('product', 'has_rounding')

        # Removing M2M table for field product_formats on 'Product'
        db.delete_table(db.shorten_name('product_product_formats'))

        # Removing M2M table for field paper on 'Product'
        db.delete_table(db.shorten_name('product_paper'))

        # Removing M2M table for field press on 'Product'
        db.delete_table(db.shorten_name('product_press'))

        # Removing M2M table for field cover_paper on 'Product'
        db.delete_table(db.shorten_name('product_cover_paper'))

        # Removing M2M table for field cover_plastic on 'Product'
        db.delete_table(db.shorten_name('product_cover_plastic'))

        # Removing M2M table for field insert_paper on 'Product'
        db.delete_table(db.shorten_name('product_insert_paper'))

        # Removing M2M table for field bindings on 'Product'
        db.delete_table(db.shorten_name('product_bindings'))

        # Removing M2M table for field flexion on 'Product'
        db.delete_table(db.shorten_name('product_flexion'))

        # Removing M2M table for field plastic on 'Product'
        db.delete_table(db.shorten_name('product_plastic'))


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
            'cover': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cover_paper': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['paper.Paper']", 'symmetrical': 'False'}),
            'cover_plastic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plastic.Plastic']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'flexion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['flexion.Flexion']", 'symmetrical': 'False'}),
            'has_binding': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_creasing': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_cutting': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_flexion': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_hole_drilling': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_improper_cutting': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_insert': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_laminating': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_mutations': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_plastic': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_rounding': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_title': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'has_vacuuming': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
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