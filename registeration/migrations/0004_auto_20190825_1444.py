# Generated by Django 2.1.9 on 2019-08-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0003_visitor_visit_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
