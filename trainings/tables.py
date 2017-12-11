import django_tables2 as tables
from django_tables2.utils import A

from trainings.models import Event


class TrainingsTable(tables.Table):
    title = tables.LinkColumn('trainings:event_detail', args=[A('pk')])

    class Meta:
        model = Event
        template = 'django_tables2/bootstrap-responsive.html'
        exclude = ['slug', 'content', 'summary', 'participants']
