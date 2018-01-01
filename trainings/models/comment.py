from django.contrib.auth.models import User
from django.db import models

from . import Event


class Comment(models.Model):

    event = models.ForeignKey(
        Event,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="wydarzenie",
        blank=True,
        default=""
    )
    author = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="autor",
        blank=True,
        default=""
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.event)
