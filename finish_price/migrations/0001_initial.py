# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FinishPrice'
        db.create_table('finish_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('finish', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['finish.Finish'])),
            ('x', self.gf('django.db.models.fields.IntegerField')()),
            ('start_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
            ('x_price', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=2)),
        ))
        db.send_create_signal(u'finish_price', ['FinishPrice'])


    def backwards(self, orm):
        # Deleting model 'FinishPrice'
        db.delete_table('finish_price')


    models = {
        u'finish.finish': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Finish', 'db_table': "'finish'"},
            'display_as_additional': ('django.db.models.fields.BooleanField', [], {}),
            'has_types': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'x': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'finish_price.finishprice': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'FinishPrice', 'db_table': "'finish_price'"},
            'finish': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['finish.Finish']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'x': ('django.db.models.fields.IntegerField', [], {}),
            'x_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'})
        }
    }

    complete_apps = ['finish_price']