# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field cover_finish on 'CartProduct'
        m2m_table_name = db.shorten_name('cart_product_cover_finish')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cartproduct', models.ForeignKey(orm[u'cart_product.cartproduct'], null=False)),
            ('finish', models.ForeignKey(orm[u'finish.finish'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cartproduct_id', 'finish_id'])

        # Adding M2M table for field cover_finish_type on 'CartProduct'
        m2m_table_name = db.shorten_name('cart_product_cover_finish_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cartproduct', models.ForeignKey(orm[u'cart_product.cartproduct'], null=False)),
            ('finishtype', models.ForeignKey(orm[u'finish_type.finishtype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['cartproduct_id', 'finishtype_id'])


    def backwards(self, orm):
        # Removing M2M table for field cover_finish on 'CartProduct'
        db.delete_table(db.shorten_name('cart_product_cover_finish'))

        # Removing M2M table for field cover_finish_type on 'CartProduct'
        db.delete_table(db.shorten_name('cart_product_cover_finish_type'))


    models = {
        u'cart.cart': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Cart', 'db_table': "'cart'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.User']"})
        },
        u'cart_product.cartproduct': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'CartProduct', 'db_table': "'cart_product'"},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cart.Cart']"}),
            'cover_finish': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'cart-product-cover-finish'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['finish.Finish']"}),
            'cover_finish_type': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'cart-product-cover-finish-type'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['finish_type.FinishType']"}),
            'cover_paper': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cart-product-cover-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'finish': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'cart-product-finish'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['finish.Finish']"}),
            'finish_type': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'cart-product-finish-type'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['finish_type.FinishType']"}),
            'format': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-format'", 'null': 'True', 'to': u"orm['format.Format']"}),
            'has_cover': ('django.db.models.fields.BooleanField', [], {}),
            'has_insert': ('django.db.models.fields.BooleanField', [], {}),
            'has_insert_print': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insert_paper': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cart-product-insert-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'insert_press': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cart-product-insert-press'", 'null': 'True', 'to': u"orm['press.Press']"}),
            'insert_volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_copies': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'number_of_inserts': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'number_of_mutation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'paper': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'press': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cart-product-press'", 'null': 'True', 'to': u"orm['press.Press']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Product']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'finish.finish': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Finish', 'db_table': "'finish'"},
            'cover': ('django.db.models.fields.BooleanField', [], {}),
            'display_as_additional': ('django.db.models.fields.BooleanField', [], {}),
            'has_types': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'x': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'finish_type.finishtype': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'FinishType', 'db_table': "'finish_type'"},
            'finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish.Finish']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'1024'"})
        },
        u'format.format': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Format', 'db_table': "'format'"},
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'product_subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_subcategory.ProductSubcategory']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['user.User']", 'null': 'True', 'blank': 'True'}),
            'user_format': ('django.db.models.fields.BooleanField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'paper.paper': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Paper', 'db_table': "'paper'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paper_finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper_finish.PaperFinish']", 'null': 'True', 'blank': 'True'}),
            'paper_thickness': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            'paper_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper_type.PaperType']"}),
            'paper_weight': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper_weight.PaperWeight']"}),
            'price_per_kilogram': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            'role': ('django.db.models.fields.BooleanField', [], {})
        },
        u'paper_finish.paperfinish': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperFinish', 'db_table': "'paper_finish'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'paper_type.papertype': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperType', 'db_table': "'paper_type'"},
            'better_quality_paper': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'paper_weight.paperweight': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperWeight', 'db_table': "'paper_weight'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'press.press': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Press', 'db_table': "'press'"},
            'both_sides_print': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'printer.printer': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Printer', 'db_table': "'printer'"},
            'color': ('django.db.models.fields.BooleanField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'press': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'printer-press'", 'symmetrical': 'False', 'to': u"orm['press.Press']"}),
            'printing_price_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'role': ('django.db.models.fields.BooleanField', [], {}),
            'user_discount': ('django.db.models.fields.BooleanField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'product.product': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Product', 'db_table': "'product'"},
            'cover_finish': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'product-cover-finish'", 'to': u"orm['finish.Finish']", 'through': u"orm['product.ProductCoverFinish']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'cover_finish_order': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'cover_finish_type': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'product_cover_finish_type'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['finish_type.FinishType']"}),
            'cover_paper': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['paper.Paper']", 'null': 'True', 'blank': 'True'}),
            'cover_printer': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'product-cover-printer'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['printer.Printer']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'finish': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'product-finish'", 'to': u"orm['finish.Finish']", 'through': u"orm['product.ProductFinish']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'finish_order': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'formats': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'product_formats'", 'null': 'True', 'to': u"orm['format.Format']"}),
            'has_cover': ('django.db.models.fields.BooleanField', [], {}),
            'has_insert': ('django.db.models.fields.BooleanField', [], {}),
            'has_mutations': ('django.db.models.fields.BooleanField', [], {}),
            'has_title': ('django.db.models.fields.BooleanField', [], {}),
            'has_volume': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'insert_paper': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'product-insert-paper'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['paper.Paper']"}),
            'insert_press': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'product-insert-press'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['press.Press']"}),
            'insert_printer': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'product-insert-printer'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['printer.Printer']"}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'paper': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'paper'", 'null': 'True', 'to': u"orm['paper.Paper']"}),
            'press': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['press.Press']", 'null': 'True', 'symmetrical': 'False'}),
            'printer': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'product-printer'", 'symmetrical': 'False', 'through': u"orm['product.ProductPrinter']", 'to': u"orm['printer.Printer']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product_subcategory.ProductSubcategory']"}),
            'turn_on_cover': ('django.db.models.fields.BooleanField', [], {})
        },
        u'product.productcoverfinish': {
            'Meta': {'object_name': 'ProductCoverFinish'},
            'finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish.Finish']"}),
            'finish_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['finish_type.FinishType']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_on': ('django.db.models.fields.BooleanField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Product']"})
        },
        u'product.productfinish': {
            'Meta': {'object_name': 'ProductFinish'},
            'finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish.Finish']"}),
            'finish_type': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['finish_type.FinishType']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_on': ('django.db.models.fields.BooleanField', [], {}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Product']"})
        },
        u'product.productprinter': {
            'Meta': {'object_name': 'ProductPrinter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['printer.Printer']"}),
            'printing_price_type': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Product']"})
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
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2', 'blank': 'True'}),
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