# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'CartProduct.hole_drilling'
        db.delete_column('cart_product', 'hole_drilling')

        # Deleting field 'CartProduct.laminating'
        db.delete_column('cart_product', 'laminating')

        # Deleting field 'CartProduct.rounding'
        db.delete_column('cart_product', 'rounding')

        # Deleting field 'CartProduct.creasing'
        db.delete_column('cart_product', 'creasing')

        # Deleting field 'CartProduct.plastic'
        db.delete_column('cart_product', 'plastic_id')

        # Deleting field 'CartProduct.improper_cutting'
        db.delete_column('cart_product', 'improper_cutting')

        # Deleting field 'CartProduct.flexion'
        db.delete_column('cart_product', 'flexion_id')

        # Deleting field 'CartProduct.cutting'
        db.delete_column('cart_product', 'cutting')

        # Deleting field 'CartProduct.vacuuming'
        db.delete_column('cart_product', 'vacuuming')


    def backwards(self, orm):
        # Adding field 'CartProduct.hole_drilling'
        db.add_column('cart_product', 'hole_drilling',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)

        # Adding field 'CartProduct.laminating'
        db.add_column('cart_product', 'laminating',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)

        # Adding field 'CartProduct.rounding'
        db.add_column('cart_product', 'rounding',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)

        # Adding field 'CartProduct.creasing'
        db.add_column('cart_product', 'creasing',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)

        # Adding field 'CartProduct.plastic'
        db.add_column('cart_product', 'plastic',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='cart-product-plastic', null=True, to=orm['plastic.Plastic'], blank=True),
                      keep_default=False)

        # Adding field 'CartProduct.improper_cutting'
        db.add_column('cart_product', 'improper_cutting',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)

        # Adding field 'CartProduct.flexion'
        db.add_column('cart_product', 'flexion',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flexion.Flexion'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'CartProduct.cutting'
        db.add_column('cart_product', 'cutting',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)

        # Adding field 'CartProduct.vacuuming'
        db.add_column('cart_product', 'vacuuming',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)


    models = {
        u'cart.cart': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Cart', 'db_table': "'cart'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.User']"})
        },
        u'cart_product.cartproduct': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CartProduct', 'db_table': "'cart_product'"},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cart.Cart']"}),
            'cover_paper': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cart-product-cover-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'cover_plastic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cart-product-cover-plastic'", 'null': 'True', 'to': u"orm['plastic.Plastic']"}),
            'format': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-format'", 'null': 'True', 'to': u"orm['format.Format']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_paper': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cart-product-insert-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'number_of_copies': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'number_of_mutation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'paper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'press': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-press'", 'null': 'True', 'to': u"orm['press.Press']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Product']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'})
        },
        u'format.format': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Format', 'db_table': "'format'"},
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product_subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_subcategory.ProductSubcategory']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.User']", 'null': 'True', 'blank': 'True'}),
            'user_format': ('django.db.models.fields.BooleanField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'paper.paper': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Paper', 'db_table': "'paper'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paper_finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper_finish.PaperFinish']", 'null': 'True', 'blank': 'True'}),
            'paper_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper_type.PaperType']"}),
            'paper_weight': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper_weight.PaperWeight']"}),
            'price_per_kilogram': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'})
        },
        u'paper_finish.paperfinish': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperFinish', 'db_table': "'paper_finish'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'paper_type.papertype': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperType', 'db_table': "'paper_type'"},
            'better_quality_paper': ('django.db.models.fields.BooleanField', [], {}),
            'has_finish': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'paper_weight.paperweight': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperWeight', 'db_table': "'paper_weight'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'plastic.plastic': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Plastic', 'db_table': "'plastic'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'press.press': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Press', 'db_table': "'press'"},
            'both_sides_print': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'product.product': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Product', 'db_table': "'product'"},
            'cover_paper': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['paper.Paper']", 'null': 'True', 'symmetrical': 'False'}),
            'cover_plastic': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['plastic.Plastic']", 'null': 'True', 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'formats': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'product-formats'", 'null': 'True', 'to': u"orm['format.Format']"}),
            'has_cover': ('django.db.models.fields.BooleanField', [], {}),
            'has_insert': ('django.db.models.fields.BooleanField', [], {}),
            'has_mutations': ('django.db.models.fields.BooleanField', [], {}),
            'has_title': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'insert_paper': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'product-insert-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'paper': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'press': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['press.Press']", 'null': 'True', 'symmetrical': 'False'}),
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
            'click_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
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
            'start_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'})
        }
    }

    complete_apps = ['cart_product']