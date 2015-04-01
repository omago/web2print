# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PaperWeight'
        db.create_table('paper_weight', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'paper_weight', ['PaperWeight'])


    def backwards(self, orm):
        # Deleting model 'PaperWeight'
        db.delete_table('paper_weight')


    models = {
        u'paper_weight.paperweight': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperWeight', 'db_table': "'paper_weight'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['paper_weight']