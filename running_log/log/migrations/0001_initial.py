# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(db_index=True)),
                ('distance', models.IntegerField(null=True, blank=True)),
                ('time', models.DurationField(null=True, blank=True)),
                ('activity_type', models.CharField(max_length=256, null=True, blank=True)),
                ('conditions', models.CharField(max_length=512, null=True, blank=True)),
                ('location', models.CharField(max_length=512, null=True, blank=True)),
                ('comments', models.CharField(max_length=512, null=True, blank=True)),
            ],
            options={
                'db_table': 'activity',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('picture', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Profile',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Races',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, null=True, blank=True)),
                ('distance', models.IntegerField(null=True, blank=True)),
                ('time', models.IntegerField(null=True, blank=True)),
                ('place', models.CharField(max_length=64, null=True, blank=True)),
                ('activity_id', models.ForeignKey(to='log.Activity')),
            ],
            options={
                'db_table': 'races',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, null=True, blank=True)),
                ('mileage', models.IntegerField(null=True, blank=True)),
                ('expiration_mileage', models.IntegerField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'shoe',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
            ],
            options={
                'db_table': 'team',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team', models.ForeignKey(to='log.Team')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interval_num', models.IntegerField()),
                ('distance', models.IntegerField(null=True, blank=True)),
                ('actual_time', models.CharField(max_length=16, null=True, blank=True)),
                ('goal_time', models.CharField(max_length=16, null=True, blank=True)),
                ('rest', models.CharField(max_length=16, null=True, blank=True)),
                ('activity_id', models.ForeignKey(to='log.Activity')),
            ],
            options={
                'db_table': 'workout',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='shoe',
            field=models.ForeignKey(blank=True, to='log.Shoe', null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='workout',
            unique_together=set([('activity_id', 'interval_num')]),
        ),
    ]
