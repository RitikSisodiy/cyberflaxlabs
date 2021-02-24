# Generated by Django 3.1.6 on 2021-02-18 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourwork', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='headbanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=5000)),
                ('title', models.CharField(max_length=100)),
                ('projectimage', models.ImageField(upload_to='ourwork/projectimage')),
                ('projectTitle', models.CharField(max_length=200)),
                ('projectsource', models.ImageField(upload_to='ourwork/projectsource')),
                ('projecticon', models.ImageField(upload_to='ourwork/projecticon')),
                ('catagory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ourwork.ourwork_cat')),
            ],
        ),
    ]