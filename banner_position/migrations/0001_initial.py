# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BannerPosition'
        db.create_table('banner_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'banner_position', ['BannerPosition'])


    def backwards(self, orm):
        # Deleting model 'BannerPosition'
        db.delete_table('banner_position')


    models = {
        u'banner_position.bannerposition': {
            'Meta': {'ordering': "['pk']", 'object_name': 'BannerPosition', 'db_table': "'banner_position'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['banner_position']