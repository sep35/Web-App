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
    url(r'^activity/new/$', views.new_activity, name='new_activity'),
    url(r'^activity/(\d+)/$', views.detail, name='detail'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^table/$', views.table, name='table'

    #### Team setup & logs ####
    url(r'^teams/$', views.teams, name='teams')

    #### Public SQL data tables ####
    url(r'^publicTable/$', views.publicTable, name='publicTable')
]
