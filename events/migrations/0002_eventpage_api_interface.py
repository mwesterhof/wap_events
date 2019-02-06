# Generated by Django 2.1.5 on 2019-02-06 15:16

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='api_interface',
            field=wagtail.core.fields.StreamField([('comment_list', wagtail.core.blocks.StructBlock([])), ('comment_submit', wagtail.core.blocks.StructBlock([]))], default=''),
            preserve_default=False,
        ),
    ]
