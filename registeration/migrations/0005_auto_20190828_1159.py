# Generated by Django 2.1.9 on 2019-08-28 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0004_auto_20190825_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='is_active',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='event',
            name='is_active',
            field=models.BooleanField(default=1),
        ),
    ]
