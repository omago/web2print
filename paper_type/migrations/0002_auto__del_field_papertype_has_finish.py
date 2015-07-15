# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PaperType.has_finish'
        db.delete_column('paper_type', 'has_finish')


    def backwards(self, orm):
        # Adding field 'PaperType.has_finish'
        db.add_column('paper_type', 'has_finish',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)


    models = {
        u'paper_type.papertype': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperType', 'db_table': "'paper_type'"},
            'better_quality_paper': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['paper_type']