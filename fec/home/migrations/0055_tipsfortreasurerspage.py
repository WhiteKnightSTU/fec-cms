# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 22:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('home', '0054_auto_20170118_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipsForTreasurersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.fields.StreamField((('heading', wagtail.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('html', wagtail.blocks.RawHTMLBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock())), blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
