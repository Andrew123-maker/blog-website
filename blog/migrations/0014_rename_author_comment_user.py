# Generated by Django 5.0.2 on 2024-05-21 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]