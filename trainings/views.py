from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, WeekArchiveView, RedirectView
from django.core.urlresolvers import reverse

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

from trainings.models import Event, Comment
from .forms import EmailEventForm, CommentForm
from .tables import TrainingsTable


def matches_list(request):
    matches = Event.matches.all()
    return render(request, 'trainings/event/list.html', {'events': matches})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    comments = event.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.event = event
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'trainings/event/detail.html', {'event': event, 'comments': comments, 'comment_form': comment_form})


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
