# Generated by Django 3.1.6 on 2021-02-18 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0013_auto_20210218_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='subproject',
            name='services',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.service'),
        ),
    ]