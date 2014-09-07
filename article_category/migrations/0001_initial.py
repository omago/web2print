# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ArticleCategory'
        db.create_table('article_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('meta_description', self.gf('django.db.models.fields.TextField')(null=True)),
            ('meta_keywords', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal(u'article_category', ['ArticleCategory'])


    def backwards(self, orm):
        # Deleting model 'ArticleCategory'
        db.delete_table('article_category')


    models = {
        u'article_category.articlecategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ArticleCategory', 'db_table': "'article_category'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['article_category']