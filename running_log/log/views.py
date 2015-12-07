# Create your views here.

from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from .forms import ActivityForm, UserForm, DateRangeForm
from .models import Activity, Team
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .tables import ActivityTable, top20Table
from django_tables2   import RequestConfig
from chartit import DataPool, Chart
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Sum
import json
import time, datetime


#### TEAM VIEWS ####

@login_required(login_url="/login/")
def teams(request):
    teams = Team.objects.all()
    return render(request, 'log/teams.html', {'teams': teams})


#### REGISTRATION + SETUP VIEWS ####

def home_page(request):
    activities = Activity.objects.all()
    return render(request, 'log/home_page.html', {'activities': activities})

def logout_view(request):
    logout(request)
    return render_to_response('log/logout.html')

def register(request):
    context = RequestContext(request)

    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()
    # Render the template depending on the context.
    return render_to_response(
            'log/registration.html',
            {'user_form': user_form, 'registered': registered},
            context)


#### USER VIEWS ####

@login_required(login_url="/login/")
def profile(request):
    context = RequestContext(request)

    u = User.objects.get(username=request.user.username)
    activities = Activity.objects.filter(user_id=request.user.id)

    return render_to_response('log/profile.html', {'u': u, 'activities': activities}, context)

@login_required(login_url="/login/")
def log(request):
    activities = Activity.objects.filter(user_id=request.user.id)
    TOP20 = User.objects.raw('''SELECT* FROM (SELECT SUM(distance) As distance, username, auth_user.id from auth_user LEFT OUTER JOIN Activity ON auth_user.id = Activity.user_id Where Activity.date BETWEEN (current_date- 6) AND current_date  Group By auth_user.id) AS B LIMIT 20;''')

    table = ActivityTable(activities, prefix="1-")
    table2 = top20Table(TOP20, prefix="2-")

    RequestConfig(request).configure(table)
    RequestConfig(request).configure(table2)

    return render(request, 'log/activity_list.html', {'table': activities, 'table2':table2})

@login_required(login_url="/login/")
def new_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            u = User.objects.get(id=request.user.id)
            post.user = u
            post.save()
            return redirect('/log/', pk=post.pk)
    else:
        form = ActivityForm()
    return render(request, 'log/activity_edit.html', {'form': form})

@login_required(login_url="/login/")
def detail(request, x):
    activity = Activity.objects.get(id=x)
    return render(request, 'log/details.html', {'activity': activity})

#### Table for custom SQL queries ####
def table(request):

    rawQueryString = 'SELECT * FROM Activity'

    rawQueryString = rawQueryString.replace('my_user_id', str(id))

    queryTuples = User.objects.raw(rawQueryString)
    columns = queryTuples.columns

    a = []
    for r in queryTuples:
        b = []
        for c in columns:
            b.append(getattr(r, c))
        a.append(b)




    return render(request, 'log/table.html', {'data': a, 'columns': columns})

### Helper Functions ###
def month_name_day(*t):
    names ={'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
            '5': 'May', '6': 'Jun', '7': 'Jul', '8': 'Aug',
            '9': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
    month_num = t[0][0]
    return (names[month_num], t[0][1])

### Graph/Charts Views ###
@login_required(login_url="/login/")
def charts(request):
      data = Activity.objects.filter(user_id=request.user.id).order_by('-date')[:20]
      mileage_per_date = Activity.objects.filter(date__range=('2013-07-26','2016-07-26')).values('date').annotate(distance=Sum('distance'))

      def month_name_day(*t):
          names ={'01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr',
                  '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug',
                  '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'}
          month_num = t[0][0]
          return (names[month_num], t[0][1])
      runtype = \
          DataPool(
             series=
              [{'options': {
                 'source': mileage_per_date},
                'terms': [
                  ('date',lambda d: (d.strftime("%m"),d.strftime("%d"))),
                  'distance']}
               ])
      cht2 = Chart(
          datasource = runtype,
          series_options =
            [{'options':{
                'type': 'column',
                'stacking': False},
              'terms':{
                'date': [
                  'distance']
                }}],
          chart_options =
            {'title': {
                 'text': 'Distance by Date'},
             'xAxis': {
                  'title': {
                     'text': 'Date'}}},
                     x_sortf_mapf_mts=(None,month_name_day, False))
      #Step 2: Create the Chart object
      pacedata = \
          DataPool(
             series=
              [{'options': {
                 'source': data},
                'terms': [
                  ('date', lambda d: (d.strftime("%m"),d.strftime("%d"))),
                  'distance']}
               ])

      cht = Chart(
              datasource = pacedata,
              series_options =
                [{'options':{
                    'type': 'line',
                    'stacking': True},
                  'terms':{
                    'date': [
                      'distance']
                    }}],
              chart_options =
                {'title': {
                     'text': 'Runs: Distance/Date '},
                 'xAxis': {
                      'title': {
                         'text': 'Date'}}},
                         x_sortf_mapf_mts=(lambda x: (x[1],x[0]),month_name_day, False))

      #Step 3: Send the chart object to the template.
      return render_to_response('log/charts.html',{'pacedata': cht2,'types':cht2},context_instance=RequestContext(request))
