# Generated by Django 5.0.2 on 2024-05-06 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.CharField(default='#Topic', max_length=20),
        ),
    ]