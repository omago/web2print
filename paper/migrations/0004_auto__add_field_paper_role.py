# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Paper.role'
        db.add_column('paper', 'role',
                      self.gf('django.db.models.fields.BooleanField')(default=None),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Paper.role'
        db.delete_column('paper', 'role')


    models = {
        u'paper.paper': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Paper', 'db_table': "'paper'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paper_finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper_finish.PaperFinish']", 'null': 'True', 'blank': 'True'}),
            'paper_thickness': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'paper_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper_type.PaperType']"}),
            'paper_weight': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paper_weight.PaperWeight']"}),
            'price_per_kilogram': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
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
            'has_finish': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'paper_weight.paperweight': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'PaperWeight', 'db_table': "'paper_weight'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['paper']