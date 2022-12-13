# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-31 20:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import home.blocks
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('home', '0100_auto_20180126_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('contact_items', wagtail.fields.StreamField((('contact_items', wagtail.blocks.StructBlock((('label', wagtail.blocks.CharBlock(icon='title', required=False)), ('contact_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('item_label', wagtail.blocks.CharBlock(required=False)), ('item_icon', wagtail.blocks.ChoiceBlock(choices=[('email', 'Email'), ('fax', 'Fax'), ('hand', 'Hand delivery'), ('phone', 'Phone'), ('mail', 'Mail'), ('github', 'Github'), ('question-bubble', 'Question')])), ('item_info', wagtail.blocks.RichTextBlock(required=True))))))))),))),
                ('services_title', models.TextField()),
                ('services', wagtail.fields.StreamField((('services', wagtail.blocks.RichTextBlock()),))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='sections',
            field=wagtail.fields.StreamField((('sections', wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock(required=True)), ('hide_title', wagtail.blocks.BooleanBlock(help_text='Should the section title be displayed?', required=False)), ('content', wagtail.blocks.StreamBlock((('text', wagtail.blocks.RichTextBlock(blank=False, icon='pilcrow', null=False, required=False)), ('documents', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock()), ('media_type', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.CharBlock()))), icon='doc-empty', template='blocks/section-documents.html')), ('contact_info', wagtail.blocks.StructBlock((('label', wagtail.blocks.CharBlock(icon='title', required=False)), ('contact_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('item_label', wagtail.blocks.CharBlock(required=False)), ('item_icon', wagtail.blocks.ChoiceBlock(choices=[('email', 'Email'), ('fax', 'Fax'), ('hand', 'Hand delivery'), ('phone', 'Phone'), ('mail', 'Mail'), ('github', 'Github'), ('question-bubble', 'Question')])), ('item_info', wagtail.blocks.RichTextBlock(required=True))))))))), ('internal_button', wagtail.blocks.StructBlock((('internal_page', wagtail.blocks.PageChooserBlock()), ('text', wagtail.blocks.CharBlock())))), ('external_button', wagtail.blocks.StructBlock((('url', wagtail.blocks.URLBlock()), ('text', wagtail.blocks.CharBlock())))), ('page', wagtail.blocks.PageChooserBlock(template='blocks/page-links.html')), ('disabled_page', wagtail.blocks.CharBlock(blank=False, help_text='Name of a disabled link', icon='placeholder', null=False, required=False, template='blocks/disabled-page-links.html')), ('document_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock((('title', wagtail.blocks.CharBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock()))), icon='doc-empty', template='blocks/document-list.html')), ('current_commissioners', home.blocks.CurrentCommissionersBlock()), ('fec_jobs', home.blocks.CareersBlock()), ('mur_search', home.blocks.MURSearchBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock()), ('html', wagtail.blocks.RawHTMLBlock()), ('reporting_example_cards', wagtail.blocks.StructBlock((('card_width', wagtail.blocks.ChoiceBlock(choices=[(2, '1/2'), (3, '1/3')], default=2, help_text='Control the width of the cards')), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(), icon='doc-empty'))))), ('contribution_limits_table', wagtail.snippets.blocks.SnippetChooserBlock('home.EmbedTableSnippet', icon='table', template='blocks/embed-table.html'))))), ('aside', wagtail.blocks.StreamBlock((('title', wagtail.blocks.CharBlock(icon='title', required=False)), ('document', wagtail.blocks.StructBlock((('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock()), ('media_type', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.CharBlock())))), ('link', wagtail.blocks.StructBlock((('link_type', wagtail.blocks.ChoiceBlock(choices=[('calculator', 'Calculator'), ('calendar', 'Calendar'), ('record', 'Record'), ('search', 'Search')], help_text='Set an icon', icon='link', required=False)), ('url', wagtail.blocks.URLBlock()), ('text', wagtail.blocks.CharBlock(required=True)), ('coming_soon', wagtail.blocks.BooleanBlock(required=False)))))), icon='placeholder', template='blocks/section-aside.html'))))),), null=True),
        ),
    ]
