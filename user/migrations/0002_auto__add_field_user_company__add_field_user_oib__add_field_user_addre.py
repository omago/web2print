# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'User.company'
        db.add_column('user', 'company',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.oib'
        db.add_column('user', 'oib',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=254),
                      keep_default=False)

        # Adding field 'User.address'
        db.add_column('user', 'address',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.e_mail'
        db.add_column('user', 'e_mail',
                      self.gf('django.db.models.fields.EmailField')(default=None, max_length=254),
                      keep_default=False)

        # Adding field 'User.phone'
        db.add_column('user', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.contact_person'
        db.add_column('user', 'contact_person',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'User.company'
        db.delete_column('user', 'company')

        # Deleting field 'User.oib'
        db.delete_column('user', 'oib')

        # Deleting field 'User.address'
        db.delete_column('user', 'address')

        # Deleting field 'User.e_mail'
        db.delete_column('user', 'e_mail')

        # Deleting field 'User.phone'
        db.delete_column('user', 'phone')

        # Deleting field 'User.contact_person'
        db.delete_column('user', 'contact_person')


    models = {
        u'user.user': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'User', 'db_table': "'user'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'e_mail': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'oib': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '254', 'db_index': 'True'})
        }
    }

    complete_apps = ['user']