# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PaperType'
        db.create_table('paper_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('has_finish', self.gf('django.db.models.fields.BooleanField')()),
            ('better_quality_paper', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'paper_type', ['PaperType'])


    def backwards(self, orm):
        # Deleting model 'PaperType'
        db.delete_table('paper_type')


    models = {
        u'paper_type.papertype': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperType', 'db_table': "'paper_type'"},
            'better_quality_paper': ('django.db.models.fields.BooleanField', [], {}),
            'has_finish': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['paper_type']