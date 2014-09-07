# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.category'
        db.delete_column('article', 'category_id')

        # Adding field 'Article.article_category'
        db.add_column('article', 'article_category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['article_category.ArticleCategory']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Article.category'
        db.add_column('article', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['article_category.ArticleCategory']),
                      keep_default=False)

        # Deleting field 'Article.article_category'
        db.delete_column('article', 'article_category_id')


    models = {
        u'article.article': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Article', 'db_table': "'article'"},
            'article_category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['article_category.ArticleCategory']"}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intro': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        },
        u'article_category.articlecategory': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'ArticleCategory', 'db_table': "'article_category'"},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'meta_keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['article']