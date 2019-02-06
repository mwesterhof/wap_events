from django.template.loader import render_to_string
from wagtail.core import blocks


class PreviewBlock(blocks.StaticBlock):
    def __init__(self, preview_template, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.preview_template = preview_template

    def render_form(self, value, *args, **kwargs):
        return render_to_string(self.preview_template, {})


class CommentListBlock(blocks.StructBlock):
    comment_list = PreviewBlock(
        preview_template='events/blocks/previews/comment_list.html')
    delete_button_text = blocks.CharBlock(default='X')

    class Meta:
        template = 'events/blocks/comment_list.html'
        icon = 'fa-header'


class CommentSubmitBlock(blocks.StructBlock):
    comment_submit = PreviewBlock(
        preview_template='events/blocks/previews/comment_submit.html')
    placeholder_text = blocks.CharBlock()
    submit_button_text = blocks.CharBlock(default='OK')

    class Meta:
        template = 'events/blocks/comment_submit.html'
