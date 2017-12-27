from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from trainings.models import Event

from .forms import CommentForm, EmailEventForm, TrainingForm
from user.models import Coach


def get_week_range(year, week):
    whole_week = []

    d = year + "-" + "W" + week
    # obliczenie poczatku i konca tygonia
    start_week = datetime.strptime(d + '-1', "%Y-W%W-%w")
    end_week = start_week + timedelta(days=6)

    while start_week <= end_week:
        whole_week.append(start_week)
        start_week += timedelta(days=1)

    return whole_week


# TODO do it simpler only min max
def get_hours_range(trainings):
    min_hour = 24
    max_hour = 0

    for t in trainings:
        max_hour = max(t.date.hour, max_hour)
        min_hour = min(t.date.hour, min_hour)

    max_hour += 2
    return min_hour, max_hour


def matches_list(request):
    matches = Event.matches.all()
    return render(request, 'trainings/event/list.html', {'events': matches})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    template = 'trainings/event/detail.html'
    comments = event.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.event = event
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'event': event,
        'comments': comments,
        'comment_form': comment_form
    }

    return render(request, template, context)


def training_share(request, event_id):
    training = get_object_or_404(Event, id=event_id, type='training')
    sent = False

    if request.method == 'POST':
        form = EmailEventForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            training_url = request.build_absolute_uri(training.get_absolute_url())
            subject = '{} ({}) reccomends you reading "{}"'.format(cd['name'], cd['email'], training.title)
            message = 'Read "{}" at {} \n\n {}\'s comments: {}'.format(training.title, training_url, cd['name'], cd['comments'])
            send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['to']])
            sent = True

    else:
        form = EmailEventForm()

    return render(request, 'trainings/event/share.html', {'training': training, 'form': form, 'sent': sent})


def event_team_week_list(request, team_id, year, week):
    template = 'trainings/training_team_list_view.html'
    user = request.user

    if user.is_authenticated and hasattr(user, 'coach'):
        seven_days = get_week_range(str(year), str(week))
        trainings = Event.objects.week_for_team(team_id, seven_days)
        min_hour, max_hour = get_hours_range(trainings)

        context = {
            'trainings': trainings,
            'seven_days': seven_days,
            'team_id': team_id,
            'team_name': user.coach.teams.filter(id=team_id).get().name,
            'hour_range': range(min_hour, max_hour),
            'previous_start_week': seven_days[0] - timedelta(days=7),
            'next_start_week': seven_days[0] + timedelta(days=7)
        }

        return render(request, template, context)
    else:
        return HttpResponse("<h1> Brak dost?pu </h1>")


def training_new(request, team_id):
    template = 'trainings/training_edit.html'
    user = request.user
    year = datetime.today().year
    week = datetime.today().isocalendar()[1]

    if user.is_authenticated and hasattr(user, 'coach'):
        coach = request.user.coach
        team = coach.teams.filter(id=team_id).get()

        if request.method == "POST":
            form = TrainingForm(request.POST)

            if form.is_valid():
                new_training = form.save(commit=False)
                new_training.author = coach
                new_training.team = team
                new_training.save()
                new_training.participants = new_training.team.players.all()
                new_training.save()
                return redirect('trainings:event-team-week-list', team_id=team_id, year=year, week=week)
            else:
                return redirect('trainings:event-team-week-list', team_id=team_id, year=year, week=week)
        else:
            form = TrainingForm(initial={
                'performer': Coach.objects.from_one_club(team.club.id).distinct(),
            })
            return render(request, template, {'form': form, })


def training_delete(request, event_id, team_id):
    year = datetime.today().year
    week = datetime.today().isocalendar()[1]
    training = get_object_or_404(Event, id=event_id)

    if request.method =='POST':
        training.delete()
        return redirect('trainings:event-team-week-list', team_id=team_id, year=year, week=week)
