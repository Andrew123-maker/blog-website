# Generated by Django 5.0.2 on 2024-05-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_delete_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='topic',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
    ]