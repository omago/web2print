# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Printer.press'
        db.delete_column('printer', 'press_id')

        # Adding M2M table for field press on 'Printer'
        m2m_table_name = db.shorten_name('printer_press')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('printer', models.ForeignKey(orm[u'printer.printer'], null=False)),
            ('press', models.ForeignKey(orm[u'press.press'], null=False))
        ))
        db.create_unique(m2m_table_name, ['printer_id', 'press_id'])


    def backwards(self, orm):
        # Adding field 'Printer.press'
        db.add_column('printer', 'press',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='printer-press', to=orm['press.Press']),
                      keep_default=False)

        # Removing M2M table for field press on 'Printer'
        db.delete_table(db.shorten_name('printer_press'))


    models = {
        u'press.press': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Press', 'db_table': "'press'"},
            'both_sides_print': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'printer.printer': {
            'Meta': {'ordering': "['-pk']", 'object_name': 'Printer', 'db_table': "'printer'"},
            'color': ('django.db.models.fields.BooleanField', [], {}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'press': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'printer-press'", 'symmetrical': 'False', 'to': u"orm['press.Press']"}),
            'user_discount': ('django.db.models.fields.BooleanField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['printer']