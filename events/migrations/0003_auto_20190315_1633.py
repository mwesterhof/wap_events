# Generated by Django 2.1.5 on 2019-03-15 16:33

from django.db import migrations
import events.blocks
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventpage_api_interface'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='api_interface',
            field=wagtail.core.fields.StreamField([('comment_list', wagtail.core.blocks.StructBlock([('comment_list', events.blocks.PreviewBlock(preview_template='events/blocks/previews/comment_list.html')), ('delete_button_text', wagtail.core.blocks.CharBlock(default='X'))])), ('comment_submit', wagtail.core.blocks.StructBlock([('comment_submit', events.blocks.PreviewBlock(preview_template='events/blocks/previews/comment_submit.html')), ('placeholder_text', wagtail.core.blocks.CharBlock()), ('submit_button_text', wagtail.core.blocks.CharBlock(default='OK'))]))]),
        ),
    ]