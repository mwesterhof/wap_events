from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)

from .models import Comment, Event


class CommentAdmin(ModelAdmin):
    model = Comment
    menu_label = 'Comments'
    list_display = ('user', 'message', 'event')
    list_filter = ('event',)
    menu_icon = 'openquote'


class EventAdmin(ModelAdmin):
    model = Event
    menu_label = 'Events'
    list_display = ('title', 'date')
    menu_icon = 'date'


class EventGroup(ModelAdminGroup):
    menu_label = 'Events'
    items = [EventAdmin, CommentAdmin]
    menu_icon = 'date'


modeladmin_register(EventGroup)
