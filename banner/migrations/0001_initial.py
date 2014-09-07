# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Banner'
        db.create_table('banner', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('banner_position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['banner_position.BannerPosition'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=128)),
        ))
        db.send_create_signal(u'banner', ['Banner'])


    def backwards(self, orm):
        # Deleting model 'Banner'
        db.delete_table('banner')


    models = {
        u'banner.banner': {
            'Meta': {'ordering': "['pk']", 'object_name': 'Banner', 'db_table': "'banner'"},
            'banner_position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['banner_position.BannerPosition']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '128'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'banner_position.bannerposition': {
            'Meta': {'ordering': "['pk']", 'object_name': 'BannerPosition', 'db_table': "'banner_position'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['banner']