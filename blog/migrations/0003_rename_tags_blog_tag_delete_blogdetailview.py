# Generated by Django 4.2.7 on 2023-12-16 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogdetailview_comment_reply_alter_category_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tags',
            new_name='tag',
        ),
        migrations.DeleteModel(
            name='BlogDetailView',
        ),
    ]
