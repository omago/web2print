# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ServiceCategory'
        db.create_table('service_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'service_category', ['ServiceCategory'])


    def backwards(self, orm):
        # Deleting model 'ServiceCategory'
        db.delete_table('service_category')


    models = {
        u'service_category.servicecategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ServiceCategory', 'db_table': "'service_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['service_category']