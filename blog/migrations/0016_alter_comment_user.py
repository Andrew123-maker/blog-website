# Generated by Django 5.0.2 on 2024-05-22 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_delete_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
