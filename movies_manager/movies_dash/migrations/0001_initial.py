# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Hall'
        db.create_table(u'movies_dash_hall', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('attendant', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'movies_dash', ['Hall'])

        # Adding model 'Movies'
        db.create_table(u'movies_dash_movies', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('hall', self.gf('django.db.models.fields.related.ForeignKey')(related_name='halls', to=orm['movies_dash.Hall'])),
        ))
        db.send_create_signal(u'movies_dash', ['Movies'])

        # Adding model 'Film'
        db.create_table(u'movies_dash_film', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('main_actor', self.gf('django.db.models.fields.CharField')(max_length=16)),
        ))
        db.send_create_signal(u'movies_dash', ['Film'])

        # Adding model 'HallFilm'
        db.create_table(u'movies_dash_hallfilm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('hall', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['movies_dash.Hall'], unique=True)),
            ('film', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['movies_dash.Film'], unique=True)),
        ))
        db.send_create_signal(u'movies_dash', ['HallFilm'])


    def backwards(self, orm):
        # Deleting model 'Hall'
        db.delete_table(u'movies_dash_hall')

        # Deleting model 'Movies'
        db.delete_table(u'movies_dash_movies')

        # Deleting model 'Film'
        db.delete_table(u'movies_dash_film')

        # Deleting model 'HallFilm'
        db.delete_table(u'movies_dash_hallfilm')


    models = {
        u'movies_dash.film': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Film'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_actor': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'movies_dash.hall': {
            'Meta': {'ordering': "('number',)", 'object_name': 'Hall'},
            'attendant': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'movies_dash.hallfilm': {
            'Meta': {'object_name': 'HallFilm'},
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'film': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['movies_dash.Film']", 'unique': 'True'}),
            'hall': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['movies_dash.Hall']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'movies_dash.movies': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Movies'},
            'hall': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'halls'", 'to': u"orm['movies_dash.Hall']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['movies_dash']