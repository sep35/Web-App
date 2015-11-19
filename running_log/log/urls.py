from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),

    # Login / logout.
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^teams/$', views.teams, name='teams'),
    #url(r'^teams/register$', views.team_register, name='team_register'),
    url(r'^activity/new/$', views.new_activity, name='new_activity'),

]
