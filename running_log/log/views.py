# Create your views here.

from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponse
from .forms import ActivityForm, UserForm
from .models import Users, Activity, Team, AuthUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .tables import ActivityTable, top20Table
from django_tables2   import RequestConfig
from chartit import DataPool, Chart

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

    u = AuthUser.objects.get(username=request.user.username)
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

### Graph Views ###


@login_required(login_url="/login/")
def charts(request):
    pacedata = \
        DataPool(
           series=
            [{'options': {
               'source': Activity.objects.filter(user_id=request.user.id)},
              'terms': [
                'time',
                'distance']}
             ])
    runtype = \
        DataPool(
           series=
            [{'options': {
               'source': Activity.objects.filter(user_id=request.user.id)},
              'terms': [
                'activity_type',
                'distance']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = pacedata,
            series_options =
              [{'options':{
                  'type': 'scatter',
                  'stacking': False},
                'terms':{
                  'time': [
                    'distance']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Runs: Distance/Time '},
               'xAxis': {
                    'title': {
                       'text': 'time'}}})
    cht2 = Chart(
        datasource = runtype,
        series_options =
          [{'options':{
              'type': 'column',
              'stacking': True},
            'terms':{
              'activity_type': [
                'distance']
              }}],
        chart_options =
          {'title': {
               'text': 'Activity Types'},
           'xAxis': {
                'title': {
                   'text': 'Type'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('log/charts.html',{'pacedata': cht,'types':cht2},context_instance=RequestContext(request))
