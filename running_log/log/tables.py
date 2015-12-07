import django_tables2 as tables
from .models import Activity
from django_tables2.utils import A
from django.utils.safestring import mark_safe

class ActivityTable(tables.Table):

    Details = tables.LinkColumn('detail',args=[A('pk')], orderable=False, empty_values=())
    class Meta:
        model = Activity
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue','width':'120%'}
        fields = ("date","activity_type", "distance", "time", "conditions", "location", "comments" )

class top5Table(tables.Table):

    username = tables.Column()
    distance = tables.Column()
    class Meta:
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue','width':'100%'}
        fields = ("username","distance")
