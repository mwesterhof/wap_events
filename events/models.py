from django.conf import settings
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail_app_pages.models import AppPageMixin
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from .blocks import CommentListBlock, CommentSubmitBlock


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    event = models.ForeignKey(
        Event, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    message = models.TextField(max_length=1000)


class EventPage(AppPageMixin, Page):
    url_config = 'events.urls'
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    api_interface = StreamField([
        ('comment_list', CommentListBlock()),
        ('comment_submit', CommentSubmitBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('api_interface')
    ]

    settings_panels = Page.settings_panels + [
        FieldPanel('event')
    ]
