# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Service.service_category'
        db.add_column('service', 'service_category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['service_category.ServiceCategory']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Service.service_category'
        db.delete_column('service', 'service_category_id')


    models = {
        u'service.service': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Service', 'db_table': "'service'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'service_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['service_category.ServiceCategory']"})
        },
        u'service_category.servicecategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ServiceCategory', 'db_table': "'service_category'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['service']