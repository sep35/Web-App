# forms
from django.contrib.auth.models import User
from .models import Activity, Shoe, Races, Workout
from django.template import RequestContext
from django.shortcuts import render,render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponse
from django import forms
import datetime
import re


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('activity_type','distance','time','shoe','conditions','location','comments')
    def save(self, commit=True):
        Activity = super(ActivityForm, self).save(commit = False)
        Activity.date = datetime.datetime.utcnow()
        if commit:
            Activity.save()
        return Activity

class DateRangeForm(forms.ModelForm):
    startDate = forms.DateField(label="Start Date")
    endDate = forms.DateField(label="End Date")

class PsqlQueryForm(forms.ModelForm):
    query = forms.CharField(label='Enter SQL query for evaluation')

    def safeQuery(self):
        a = re.compile(r'.*(DROP|INSERT|DELETE|;)', re.I)
        if a.match(self.query):
            msg = "You wouldn't try an SQL injection attack on a bear."
            raise forms.ValidationError("Possible database corrupting query")
        return self.query

class RacesForm(forms.ModelForm):
    class Meta:
        model = Races
        fields = ('name','distance','time','place')
    def save(self, commit=True):
        Races = super(RacesForm, self).save(commit = False)
        if commit:
            Races.save()
        return Races

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ('name','mileage','expiration_mileage')
    def save(self, commit=True):
        Shoe = super(ShoeForm, self).save(commit = False)
        if commit:
            Shoe.save()
        return Shoe

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label="password",widget=forms.PasswordInput())
    password2 = forms.CharField(label="re-enter password",widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            msg = "Passwords don't match"
            raise forms.ValidationError("Password mismatch")
        return password2

    def save(self, commit=True):
        user = super(UserForm, self).save(commit = False)
        user.is_staff = False
        user.is_active = True
        user.is_superuser = False
        user.set_password(self.clean_password2())
        user.date_joined = datetime.datetime.utcnow()
        if commit:
            user.save()
        return user

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ('distance','actual_time','goal_time','rest')
    def save(self, commit=True):
        Workout = super(WorkoutForm, self).save(commit = False)
        if commit:
            Workout.save()
        return Workout
