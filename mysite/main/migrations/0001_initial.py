# Generated by Django 3.0.5 on 2021-06-03 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutorial_title', models.CharField(max_length=200)),
                ('tutorial_content', models.TextField()),
                ('tutorial_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
    ]
