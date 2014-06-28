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

        # Adding model 'Sales'
        db.create_table('orders_sales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Stock'], unique=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2000)),
        ))
        db.send_create_signal('orders', ['Sales'])

        # Adding model 'StatusOrders'
        db.create_table('orders_statusorders', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('items', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date_and_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('waiter', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('bartender', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('orders', ['StatusOrders'])


    def backwards(self, orm):
        # Deleting model 'Stock'
        db.delete_table('orders_stock')

        # Deleting model 'Sales'
        db.delete_table('orders_sales')

        # Deleting model 'StatusOrders'
        db.delete_table('orders_statusorders')


    models = {
        'orders.sales': {
            'Meta': {'object_name': 'Sales'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['orders.Stock']", 'unique': 'True'})
        },
        'orders.statusorders': {
            'Meta': {'object_name': 'StatusOrders'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'bartender': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'date_and_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'waiter': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'orders.stock': {
            'Meta': {'object_name': 'Stock'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['orders']