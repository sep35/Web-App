# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    #activity_id = models.AutoField(primary_key=True)
    date = models.DateField(db_index=True)
    user = models.ForeignKey(User)
    distance = models.IntegerField(blank=True, null=True)
    time = models.DurationField(blank=True, null=True)
    shoe = models.ForeignKey('Shoe', blank=True, null=True)
    activity_type = models.CharField(max_length=256, blank=True, null=True)
    conditions = models.CharField(max_length=512, blank=True, null=True)
    location = models.CharField(max_length=512, blank=True, null=True)
    comments = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return self.activity_type
    def __str__(self):
        return self.comments
    def __str__(self):
        return self.location
    def __str__(self):
        return self.conditions

    class Meta:
        managed = True
        db_table = 'activity'

class Profile(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=200)
    picture = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Profile'


class Races(models.Model):
    activity_id = models.ForeignKey(Activity, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'races'


class Shoe(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    shoe_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    expiration_mileage = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'shoe'


class Team(models.Model):
    name = models.CharField(unique=True, max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'team'



class Workout(models.Model):
    activity_id = models.ForeignKey(Activity)
    interval_num = models.IntegerField()
    distance = models.IntegerField(blank=True, null=True)
    actual_time = models.CharField(max_length=256, blank=True, null=True)
    goal_time = models.CharField(max_length=256, blank=True, null=True)
    rest = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'workout'
        unique_together = (('activity_id', 'interval_num'),)
