from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView, ListView, TemplateView


class MainRedirectView(RedirectView):
    query_string = True

    def get_redirect_url(self):
        # year = str(datetime.today().year)
        # week = str(datetime.today().isocalendar()[1])
        user = self.request.user

        if user.is_authenticated:
            # TODO what if is both:
            if user.groups.filter(name="Trenerzy").exists():
                return reverse('main:coach-view')  # , args=(year, week))
            elif user.groups.filter(name="Zawodnicy").exists():
                return reverse('main:player-view')  # , args=(year, week))
                # else
        else:
            return HttpResponseRedirect("/accounts/login/")
            # return reverse('main:login')


class CoachView(ListView):
    pass


class PlayerView(TemplateView):
    template_name = "main/playerView.html"







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
        my_trainings = Event.trainings.filter(Q(author=user) | Q(performer=user))
        return my_trainings

    def get_context_data(self, **kwargs):
        context = super(CoachDashboardWeekArchiveView, self).get_context_data(**kwargs)
        context['whole_week'] = week_range(self.kwargs['year'], self.kwargs['week'])
        context['header_style'] = "coachHeader"
        context['role'] = "coach"
        return context