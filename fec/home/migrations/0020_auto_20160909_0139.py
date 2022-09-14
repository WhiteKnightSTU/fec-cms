# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-09 01:39
from __future__ import unicode_literals

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20160908_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionpage',
            name='sections',
            field=wagtail.fields.StreamField((('section', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.ChoiceBlock(choices=[('check', 'Checklist'), ('bullet', 'Bulleted list')], default='bullet')), ('intro', wagtail.blocks.RichTextBlock(blank=False, null=False, required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock(classname='nothing')))))),)),
        ),
    ]
