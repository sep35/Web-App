from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),

    # Login / logout.
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_view, name='logout'),

    #url(r'^$', views.activity_list, name='activity_list'),
    url(r'^activity/new/$', views.new_activity, name='new_activity'),
    url(r'^register/$', views.register, name='register'),
]
