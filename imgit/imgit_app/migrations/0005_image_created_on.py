# Generated by Django 2.2.4 on 2019-08-08 00:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imgit_app', '0004_auto_20190808_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
