from django.conf.urls import url
from . import views

urlpatterns = [

    #### Registration and setup ####
    url(r'^$', views.home_page, name='home_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_view, name='logout'),

    #### User Log ####
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^log/$', views.log, name='log'),
    url(r'^activity/new/$', views.newActivity, name='newActivity'),
    url(r'^activity/new/race$', views.newRaceActivity, name='newRaceActivity'),
    url(r'^activity/(\d+)/$', views.detail, name='detail'),
    url(r'^activity/delete/(?P<id>\d+)/$', views.delete, name='delete_activity'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^shoe/new/$', views.newShoe, name='newShoe'),
    #### Team setup & logs ####
    url(r'^teams/$', views.teams, name='teams'),

    #### Public SQL data tables ####
    url(r'^query/$', views.queryRequest, name='query'),
    url(r'^table/$', views.table, name='table')
]
