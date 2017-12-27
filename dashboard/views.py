from datetime import datetime, timedelta
from user.models import Coach, Player

from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import RedirectView, WeekArchiveView

from trainings.models import Event


def week_range(year, week):
    whole_week = []

    d = year + "-" + "W" + week
    # obliczenie poczatku i konca tygonia
    start_week = datetime.strptime(d + '-1', "%Y-W%W-%w")
    end_week = start_week + timedelta(days=6)

    while start_week <= end_week:
        whole_week.append(start_week)
        start_week += timedelta(days=1)

    return whole_week


class DashboardRedirectView(RedirectView):
    # Whether to pass along the GET query string to the new location. 
    # If True, then the query string is appended to the URL. 
    # If False, then the query string is discarded. 
    # By default, query_string is False.
    query_string = True

    def get_redirect_url(self):
        year = str(datetime.today().year)
        week = str(datetime.today().isocalendar()[1])
        user = self.request.user

        if user.is_authenticated:
            # TODO what if is both:
            if hasattr(user, 'coach'):
                return reverse('dashboard:coach-week', args=(year, week))
            elif hasattr(user, 'player'):
                return reverse('dashboard:player-week', args=(year, week))
        else:
            return reverse_lazy('account_login')


class CoachDashboardWeekArchiveView(WeekArchiveView):
    context_object_name = 'events'
    date_field = "date"
    week_format = "%W"
    allow_future = True
    allow_empty = True
    template_name = 'dashboard/weekView.html'

    def get_queryset(self):
        user = self.request.user
        # TODO i to tylko z tego tygodnia
        my_trainings = Event.trainings.filter(Q(author=user.coach) | Q(performer=user.coach))
        return my_trainings

    def get_context_data(self, **kwargs):
        context = super(CoachDashboardWeekArchiveView, self).get_context_data(**kwargs)
        context['whole_week'] = week_range(self.kwargs['year'], self.kwargs['week'])
        context['header_style'] = "coachHeader"
        context['role'] = "coach"
        context['players'] = Player.objects.all()
        context['coaches'] = Coach.objects.all()
        return context


class PlayerDashboardWeekArchiveView(WeekArchiveView):
    context_object_name = 'events'
    date_field = "date"
    week_format = "%W"
    allow_future = True
    allow_empty = True
    template_name = 'dashboard/weekView.html'

    def get_queryset(self):
        user = self.request.user
        # TODO ?eby pobiera? tylko z tego tygodnia !
        my_trainings = user.participate_events.all()
        return my_trainings

    def get_context_data(self, **kwargs):
        context = super(PlayerDashboardWeekArchiveView, self).get_context_data(**kwargs)
        context['whole_week'] = week_range(self.kwargs['year'], self.kwargs['week'])
        context['header_style'] = "playerHeader"
        return context
