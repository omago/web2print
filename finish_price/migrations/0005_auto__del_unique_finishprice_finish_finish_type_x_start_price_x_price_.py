# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'FinishPrice', fields ['finish', 'finish_type', 'x', 'start_price', 'x_price']
        db.delete_unique('finish_price', ['finish_id', 'finish_type_id', 'x', 'start_price', 'x_price'])

        # Adding unique constraint on 'FinishPrice', fields ['finish', 'finish_type', 'x']
        db.create_unique('finish_price', ['finish_id', 'finish_type_id', 'x'])


    def backwards(self, orm):
        # Removing unique constraint on 'FinishPrice', fields ['finish', 'finish_type', 'x']
        db.delete_unique('finish_price', ['finish_id', 'finish_type_id', 'x'])

        # Adding unique constraint on 'FinishPrice', fields ['finish', 'finish_type', 'x', 'start_price', 'x_price']
        db.create_unique('finish_price', ['finish_id', 'finish_type_id', 'x', 'start_price', 'x_price'])


    models = {
        u'finish.finish': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Finish', 'db_table': "'finish'"},
            'cover': ('django.db.models.fields.BooleanField', [], {}),
            'display_as_additional': ('django.db.models.fields.BooleanField', [], {}),
            'has_types': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'x': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'finish_price.finishprice': {
            'Meta': {'ordering': "['-pk']", 'unique_together': "(('finish', 'finish_type', 'x'),)", 'object_name': 'FinishPrice', 'db_table': "'finish_price'"},
            'finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish.Finish']"}),
            'finish_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish_type.FinishType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'x_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'})
        },
        u'finish_type.finishtype': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'FinishType', 'db_table': "'finish_type'"},
            'finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish.Finish']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'1024'"})
        }
    }

    complete_apps = ['finish_price']