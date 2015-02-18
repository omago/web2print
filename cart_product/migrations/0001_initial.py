# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CartProduct'
        db.create_table('cart_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cart.Cart'])),
            ('product', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.Product'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024, null=True)),
            ('format', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cart-product-product-format', null=True, to=orm['product_format.ProductFormat'])),
            ('paper', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cart-product-paper', null=True, to=orm['paper.Paper'])),
            ('press', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cart-product-press', null=True, to=orm['press.Press'])),
            ('number_of_copies', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('number_of_mutation', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('cover_paper', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cart-product-cover-paper', null=True, to=orm['press.Press'])),
            ('cover_plastic', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cart-product-cover-plastic', null=True, to=orm['plastic.Plastic'])),
            ('insert_paper', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cart-product-insert-paper', null=True, to=orm['paper.Paper'])),
            ('cutting', self.gf('django.db.models.fields.BooleanField')()),
            ('improper_cutting', self.gf('django.db.models.fields.BooleanField')()),
            ('creasing', self.gf('django.db.models.fields.BooleanField')()),
            ('hole_drilling', self.gf('django.db.models.fields.BooleanField')()),
            ('vacuuming', self.gf('django.db.models.fields.BooleanField')()),
            ('laminating', self.gf('django.db.models.fields.BooleanField')()),
            ('rounding', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'cart_product', ['CartProduct'])

        # Adding M2M table for field bindings on 'CartProduct'
        m2m_table_name = db.shorten_name('cart_product_bindings')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cartproduct', models.ForeignKey(orm[u'cart_product.cartproduct'], null=False)),
            ('binding', models.ForeignKey(orm[u'binding.binding'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cartproduct_id', 'binding_id'])

        # Adding M2M table for field flexion on 'CartProduct'
        m2m_table_name = db.shorten_name('cart_product_flexion')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cartproduct', models.ForeignKey(orm[u'cart_product.cartproduct'], null=False)),
            ('flexion', models.ForeignKey(orm[u'flexion.flexion'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cartproduct_id', 'flexion_id'])

        # Adding M2M table for field plastic on 'CartProduct'
        m2m_table_name = db.shorten_name('cart_product_plastic')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cartproduct', models.ForeignKey(orm[u'cart_product.cartproduct'], null=False)),
            ('plastic', models.ForeignKey(orm[u'plastic.plastic'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cartproduct_id', 'plastic_id'])


    def backwards(self, orm):
        # Deleting model 'CartProduct'
        db.delete_table('cart_product')

        # Removing M2M table for field bindings on 'CartProduct'
        db.delete_table(db.shorten_name('cart_product_bindings'))

        # Removing M2M table for field flexion on 'CartProduct'
        db.delete_table(db.shorten_name('cart_product_flexion'))

        # Removing M2M table for field plastic on 'CartProduct'
        db.delete_table(db.shorten_name('cart_product_plastic'))


    models = {
        u'binding.binding': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Binding', 'db_table': "'binding'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'cart.cart': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Cart', 'db_table': "'cart'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.User']"})
        },
        u'cart_product.cartproduct': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CartProduct', 'db_table': "'cart_product'"},
            'bindings': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['binding.Binding']", 'null': 'True', 'symmetrical': 'False'}),
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cart.Cart']"}),
            'cover_paper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-cover-paper'", 'null': 'True', 'to': u"orm['press.Press']"}),
            'cover_plastic': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-cover-plastic'", 'null': 'True', 'to': u"orm['plastic.Plastic']"}),
            'creasing': ('django.db.models.fields.BooleanField', [], {}),
            'cutting': ('django.db.models.fields.BooleanField', [], {}),
            'flexion': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['flexion.Flexion']", 'null': 'True', 'symmetrical': 'False'}),
            'format': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-product-format'", 'null': 'True', 'to': u"orm['product_format.ProductFormat']"}),
            'hole_drilling': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'improper_cutting': ('django.db.models.fields.BooleanField', [], {}),
            'insert_paper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-insert-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'laminating': ('django.db.models.fields.BooleanField', [], {}),
            'number_of_copies': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'number_of_mutation': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'paper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'plastic': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'cart-product-plastic'", 'null': 'True', 'to': u"orm['plastic.Plastic']"}),
            'press': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-press'", 'null': 'True', 'to': u"orm['press.Press']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Product']"}),
            'rounding': ('django.db.models.fields.BooleanField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True'}),
            'vacuuming': ('django.db.models.fields.BooleanField', [], {})
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
            'bindings': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'product-bindings'", 'null': 'True', 'to': u"orm['binding.Binding']"}),
            'cover_paper': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['paper.Paper']", 'null': 'True', 'symmetrical': 'False'}),
            'cover_plastic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plastic.Plastic']", 'null': 'True', 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'flexion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'product-flexion'", 'null': 'True', 'to': u"orm['flexion.Flexion']"}),
            'has_binding': ('django.db.models.fields.BooleanField', [], {}),
            'has_cover': ('django.db.models.fields.BooleanField', [], {}),
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
            'insert_paper': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'product-insert-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'paper': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'plastic': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'product-plastic'", 'null': 'True', 'to': u"orm['plastic.Plastic']"}),
            'press': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['press.Press']", 'null': 'True', 'symmetrical': 'False'}),
            'product_formats': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'product-product-formats'", 'null': 'True', 'to': u"orm['product_format.ProductFormat']"}),
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
        },
        u'user.user': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'User', 'db_table': "'user'"},
            'activation_code': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'e_mail': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'oib': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'reset_password_code': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'reset_password_code_expiration': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'})
        }
    }

    complete_apps = ['cart_product']