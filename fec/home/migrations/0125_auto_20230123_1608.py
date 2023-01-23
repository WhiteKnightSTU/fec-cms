# Generated by Django 3.2.16 on 2023-01-23 21:08

from django.db import migrations
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.documents.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0124_auto_20220706_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutlandingpage',
            name='sections',
            field=wagtail.fields.StreamField([('sections', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('intro', wagtail.blocks.RichTextBlock(blank=False, null=False, required=False)), ('button_text', wagtail.blocks.CharBlock(blank=False, null=False, required=False)), ('related_page', wagtail.blocks.PageChooserBlock(required=False))]))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='collectionpage',
            name='related_pages',
            field=wagtail.fields.StreamField([('related_pages', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock()))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='collectionpage',
            name='reporting_examples',
            field=wagtail.fields.StreamField([('reporting_examples', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.RichTextBlock(help_text='Use Shift + Enter to add line breaks between citation and description'))])))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='collectionpage',
            name='sections',
            field=wagtail.fields.StreamField([('section', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.ChoiceBlock(choices=[('check', 'Checklist'), ('bullet', 'Bulleted list')])), ('intro', wagtail.blocks.RichTextBlock(blank=False, null=False, required=False)), ('items', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock(form_classname='nothing')))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='commissionerpage',
            name='commissioner_bio',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='contact_items',
            field=wagtail.fields.StreamField([('contact_items', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(icon='title', required=False)), ('contact_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('item_label', wagtail.blocks.CharBlock(required=False)), ('item_icon', wagtail.blocks.ChoiceBlock(choices=[('email', 'Email'), ('fax', 'Fax'), ('hand', 'Hand delivery'), ('phone', 'Phone'), ('mail', 'Mail'), ('github', 'Github'), ('question-bubble', 'Question')])), ('item_info', wagtail.blocks.RichTextBlock(required=True))])))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='info_message',
            field=wagtail.fields.StreamField([('informational_message', wagtail.snippets.blocks.SnippetChooserBlock('home.EmbedSnippet', icon='warning', required=False, template='blocks/embed-info-message.html'))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='services',
            field=wagtail.fields.StreamField([('services', wagtail.blocks.RichTextBlock())], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title', icon='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('html', wagtail.blocks.RawHTMLBlock()), ('example_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('caption', wagtail.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'})), ('example_paragraph', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('paragraph', wagtail.blocks.RichTextBlock(required=True))])), ('example_forms', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('forms', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock()), ('media_type', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.CharBlock())])))])), ('reporting_example_cards', wagtail.blocks.StructBlock([('card_width', wagtail.blocks.ChoiceBlock(choices=[(2, '1/2'), (3, '1/3')], help_text='Control the width of the cards')), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(), icon='doc-empty'))])), ('contact_info', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(icon='title', required=False)), ('contact_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('item_label', wagtail.blocks.CharBlock(required=False)), ('item_icon', wagtail.blocks.ChoiceBlock(choices=[('email', 'Email'), ('fax', 'Fax'), ('hand', 'Hand delivery'), ('phone', 'Phone'), ('mail', 'Mail'), ('github', 'Github'), ('question-bubble', 'Question')])), ('item_info', wagtail.blocks.RichTextBlock(required=True))])))])), ('internal_button', wagtail.blocks.StructBlock([('internal_page', wagtail.blocks.PageChooserBlock()), ('text', wagtail.blocks.CharBlock())])), ('external_button', wagtail.blocks.StructBlock([('url', wagtail.blocks.URLBlock()), ('text', wagtail.blocks.CharBlock())])), ('contribution_limits_table', wagtail.snippets.blocks.SnippetChooserBlock('home.EmbedSnippet', icon='table', template='blocks/embed-table.html')), ('informational_message', wagtail.snippets.blocks.SnippetChooserBlock('home.EmbedSnippet', icon='warning', template='blocks/embed-info-message.html')), ('document_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())]), icon='doc-empty', template='blocks/document-list.html')), ('simple_document_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('document', wagtail.documents.blocks.DocumentChooserBlock())]), icon='doc-empty', template='blocks/simple-document-list.html'))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='citations',
            field=wagtail.fields.StreamField([('citations', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.RichTextBlock(help_text='Use Shift + Enter to add line breaks between citation and description'))])))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='continue_learning',
            field=wagtail.fields.StreamField([('continue_learning', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock()), ('media_type', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.CharBlock())]), icon='doc-empty'))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='record_articles',
            field=wagtail.fields.StreamField([('record_articles', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(page_type=['home.RecordPage'])))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='custompage',
            name='related_topics',
            field=wagtail.fields.StreamField([('related_topics', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(label='Related topic')))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='documentfeedpage',
            name='intro',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='examplepage',
            name='body',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('example_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=False)), ('caption', wagtail.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True))])), ('reporting_example_cards', wagtail.blocks.StructBlock([('card_width', wagtail.blocks.ChoiceBlock(choices=[(2, '1/2'), (3, '1/3')], help_text='Control the width of the cards')), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(), icon='doc-empty'))])), ('internal_button', wagtail.blocks.StructBlock([('internal_page', wagtail.blocks.PageChooserBlock()), ('text', wagtail.blocks.CharBlock())])), ('external_button', wagtail.blocks.StructBlock([('url', wagtail.blocks.URLBlock()), ('text', wagtail.blocks.CharBlock())])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('html', wagtail.blocks.RawHTMLBlock())], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='examplepage',
            name='related_media',
            field=wagtail.fields.StreamField([('continue_learning', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('url', wagtail.blocks.URLBlock()), ('media_type', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.CharBlock())]), icon='doc-empty', template='blocks/related-media.html'))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='fullwidthpage',
            name='citations',
            field=wagtail.fields.StreamField([('citations', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.RichTextBlock(help_text='Use Shift + Enter to add line breaks between citation and description'))])))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='meetingpage',
            name='agenda',
            field=wagtail.fields.StreamField([('agenda_item', wagtail.blocks.StructBlock([('item_title', wagtail.blocks.TextBlock(required=True)), ('item_text', wagtail.blocks.RichTextBlock(required=False)), ('item_audio', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('item_video', wagtail.blocks.URLBlock(help_text='Add a YouTube URL to a specific                time in a video for this agenda item', required=False))]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='meetingpage',
            name='imported_html',
            field=wagtail.fields.StreamField([('html_block', wagtail.blocks.RawHTMLBlock())], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='meetingpage',
            name='info_message',
            field=wagtail.fields.StreamField([('informational_message', wagtail.snippets.blocks.SnippetChooserBlock('home.EmbedSnippet', icon='warning', required=False, template='blocks/embed-info-message.html'))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='meetingpage',
            name='sunshine_act_doc_upld',
            field=wagtail.fields.StreamField([('sunshine_act_upld', wagtail.documents.blocks.DocumentChooserBlock(required=False))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='oiglandingpage',
            name='resources',
            field=wagtail.fields.StreamField([('html', wagtail.blocks.RawHTMLBlock(label='OIG resources'))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='oiglandingpage',
            name='stats_content',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(form_classname='full title', icon='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('html', wagtail.blocks.RawHTMLBlock(label='HTML')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'})), ('custom_table', wagtail.blocks.StructBlock([('custom_table', wagtail.blocks.StreamBlock([('title', wagtail.blocks.CharBlock(icon='title', required=False)), ('table_intro', wagtail.blocks.RichTextBlock(required=False)), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'colHeaders': True, 'height': 108, 'language': 'en', 'renderer': 'html', 'rowHeaders': True, 'startCols': 6, 'startRows': 7})), ('footnote', wagtail.blocks.CharBlock(icon='superscript', required=False))]))]))], blank=True, help_text='If this section is empty, the logo will be shown (for screens larger than phones)', null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='oiglandingpage',
            name='you_might_also_like',
            field=wagtail.fields.StreamField([('group', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock()), ('url', wagtail.blocks.URLBlock())]), icon='list-ul', label='Group/column'))], blank=True, help_text='Expects three groups/columns but will accept fewer', null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='presslandingpage',
            name='option_blocks',
            field=wagtail.fields.StreamField([('option_blocks', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('intro', wagtail.blocks.RichTextBlock(blank=False, null=False, required=False)), ('button_text', wagtail.blocks.CharBlock(blank=False, null=False, required=False)), ('related_page', wagtail.blocks.PageChooserBlock(required=False))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='reportslandingpage',
            name='document_feeds',
            field=wagtail.fields.StreamField([('document_feed_blurb', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock()), ('description', wagtail.blocks.CharBlock())]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='reportslandingpage',
            name='intro',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='citations',
            field=wagtail.fields.StreamField([('citations', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock()), ('content', wagtail.blocks.RichTextBlock(help_text='Use Shift + Enter to add line breaks between citation and description'))])))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='intro',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='related_pages',
            field=wagtail.fields.StreamField([('related_pages', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock())), ('external_page', wagtail.blocks.RichTextBlock())], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='resourcepage',
            name='related_topics',
            field=wagtail.fields.StreamField([('related_topics', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(label='Related topic')))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='serviceslandingpage',
            name='intro',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock())], null=True, use_json_field=True),
        ),
    ]
