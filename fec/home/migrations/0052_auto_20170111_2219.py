# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 22:19
# Altered to delete migration unrelated to the Tips for Treasurers feature.
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import wagtail.contrib.table_block.blocks
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('home', '0051_commissionerpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipsForTreasurersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'html', wagtail.wagtailcore.blocks.RawHTMLBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'table', wagtail.contrib.table_block.blocks.TableBlock())], blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
