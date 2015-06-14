# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FinishPrice.finish_type'
        db.add_column('finish_price', 'finish_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finish_type.FinishType'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FinishPrice.finish_type'
        db.delete_column('finish_price', 'finish_type_id')


    models = {
        u'finish.finish': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Finish', 'db_table': "'finish'"},
            'display_as_additional': ('django.db.models.fields.BooleanField', [], {}),
            'has_types': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'x': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'finish_price.finishprice': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'FinishPrice', 'db_table': "'finish_price'"},
            'finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish.Finish']"}),
            'finish_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish_type.FinishType']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'x_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'})
        },
        u'finish_type.finishtype': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'FinishType', 'db_table': "'finish_type'"},
            'finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish.Finish']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'1024'"})
        }
    }

    complete_apps = ['finish_price']