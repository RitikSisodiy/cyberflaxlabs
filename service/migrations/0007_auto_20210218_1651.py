# Generated by Django 3.1.6 on 2021-02-18 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_auto_20210218_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_serviceweoffer',
            name='subservices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.subservices'),
        ),
    ]