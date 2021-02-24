# Generated by Django 3.1.6 on 2021-02-18 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_auto_20210218_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devlifecycle',
            name='subservices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicesubmenu'),
        ),
        migrations.AlterField(
            model_name='engagement',
            name='subservices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicesubmenu'),
        ),
        migrations.AlterField(
            model_name='servicefact',
            name='subservices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicesubmenu'),
        ),
        migrations.AlterField(
            model_name='sub_benifit',
            name='subservices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicesubmenu'),
        ),
        migrations.AlterField(
            model_name='whatwedo',
            name='subservices',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.servicesubmenu'),
        ),
    ]