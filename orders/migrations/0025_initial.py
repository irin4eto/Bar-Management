# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stock'
        db.create_table('orders_stock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal('orders', ['Stock'])

        # Adding model 'StatusOrders'
        db.create_table('orders_statusorders', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('items', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date_and_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('waiter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['waiter.Waiter'], unique=True)),
            ('bartender', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bartender.Bartender'], unique=True)),
        ))
        db.send_create_signal('orders', ['StatusOrders'])


    def backwards(self, orm):
        # Deleting model 'Stock'
        db.delete_table('orders_stock')

        # Deleting model 'StatusOrders'
        db.delete_table('orders_statusorders')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'bartender.bartender': {
            'Meta': {'object_name': 'Bartender'},
            'bartender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'orders.statusorders': {
            'Meta': {'object_name': 'StatusOrders'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'bartender': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bartender.Bartender']", 'unique': 'True'}),
            'date_and_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'waiter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['waiter.Waiter']", 'unique': 'True'})
        },
        'orders.stock': {
            'Meta': {'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'waiter.waiter': {
            'Meta': {'object_name': 'Waiter'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'waiter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['orders']