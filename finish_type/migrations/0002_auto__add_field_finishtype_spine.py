# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'FinishType.spine'
        db.add_column('finish_type', 'spine',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'FinishType.spine'
        db.delete_column('finish_type', 'spine')


    models = {
        u'finish.finish': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Finish', 'db_table': "'finish'"},
            'affects_assembly_in_press': ('django.db.models.fields.BooleanField', [], {}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'1024'"}),
            'spine': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['finish_type']