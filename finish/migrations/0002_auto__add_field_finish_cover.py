# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Finish.cover'
        db.add_column('finish', 'cover',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Finish.cover'
        db.delete_column('finish', 'cover')


    models = {
        u'finish.finish': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Finish', 'db_table': "'finish'"},
            'cover': ('django.db.models.fields.BooleanField', [], {}),
            'display_as_additional': ('django.db.models.fields.BooleanField', [], {}),
            'has_types': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'x': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['finish']