# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PaperCategory'
        db.create_table('paper_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'paper_category', ['PaperCategory'])


    def backwards(self, orm):
        # Deleting model 'PaperCategory'
        db.delete_table('paper_category')


    models = {
        u'paper_category.papercategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperCategory', 'db_table': "'paper_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['paper_category']