# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NumberOfColors'
        db.create_table('number_of_colors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'number_of_colors', ['NumberOfColors'])


    def backwards(self, orm):
        # Deleting model 'NumberOfColors'
        db.delete_table('number_of_colors')


    models = {
        u'number_of_colors.numberofcolors': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'NumberOfColors', 'db_table': "'number_of_colors'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['number_of_colors']