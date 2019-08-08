# Generated by Django 2.2.4 on 2019-08-06 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registeration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='hotel',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='agancy',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='detail_type',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='person',
            name='guide_id',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='national_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_type',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='student_id',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='study_field',
            field=models.CharField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='university',
            field=models.CharField(default='-', max_length=100),
        ),
    ]