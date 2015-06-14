# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FinishType'
        db.create_table('finish_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('finish', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finish.Finish'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length='1024')),
        ))
        db.send_create_signal(u'finish_type', ['FinishType'])


    def backwards(self, orm):
        # Deleting model 'FinishType'
        db.delete_table('finish_type')


    models = {
        u'finish.finish': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Finish', 'db_table': "'finish'"},
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
        }
    }

    complete_apps = ['finish_type']