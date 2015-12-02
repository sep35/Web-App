# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Activity(models.Model):
    #activity_id = models.AutoField(primary_key=True)
    date = models.DateField()
    user = models.ForeignKey(User)
    distance = models.IntegerField(blank=True, null=True)
    t = models.DurationField(blank=True, null=True)
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
        managed = False
        db_table = 'activity'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.ForeignKey(AuthGroup)
    permission_id = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    def __str__(self):
        return self.first_name
    def __str__(self):
        return self.last_name
    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.ForeignKey(AuthUser)
    group_id = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.ForeignKey(AuthUser)
    permission_id = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LogUser(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'log_user'


class Races(models.Model):
    activity_id = models.ForeignKey(Activity, blank=True, null=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    place = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'races'


class Shoe(models.Model):
    shoe_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, blank=True, null=True)
    mileage = models.IntegerField(blank=True, null=True)
    expiration_mileage = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'shoe'


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'team'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    email = models.CharField(unique=True, max_length=256)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.emaiil

    class Meta:
        managed = False
        db_table = 'users'


class Workout(models.Model):
    activity_id = models.ForeignKey(Activity,default=0)
    interval_num = models.IntegerField()
    distance = models.IntegerField(blank=True, null=True)
    actual_time = models.CharField(max_length=256, blank=True, null=True)
    goal_time = models.CharField(max_length=256, blank=True, null=True)
    rest = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'workout'
        unique_together = (('activity_id', 'interval_num'),)
