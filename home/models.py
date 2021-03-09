from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from .blocks import FooBlock


# Foo
#  Bar1
#  Bar2


class HomePage(Page):
    pass


class ReactDemoPage(Page):
    api_interface = StreamField([
        ('foo', FooBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('api_interface')
    ]
