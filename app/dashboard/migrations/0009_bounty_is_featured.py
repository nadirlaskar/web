# Generated by Django 2.1.4 on 2019-01-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20190120_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='bounty',
            name='is_featured',
            field=models.BooleanField(default=False, help_text='Whether this bounty is featured'),
        ),
    ]