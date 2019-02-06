from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Event


class EventAdmin(ModelAdmin):
    model = Event
    menu_label = 'Events'
    list_display = ('title', 'date')


modeladmin_register(EventAdmin)
