# Generated by Django 3.2.7 on 2021-09-17 11:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demorestapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 9, 17, 11, 21, 25, 962729, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
