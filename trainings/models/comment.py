from django.db import models

from . import Event

# from trainings.models.event import Event


class Comment(models.Model):

    # The name to use for the relation from the related object back to this one. I
    event = models.ForeignKey(Event, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.event)
