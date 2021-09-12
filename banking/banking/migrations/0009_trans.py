# Generated by Django 3.1.6 on 2021-09-11 16:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0008_auto_20210911_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('account', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=15)),
                ('balance', models.CharField(max_length=20)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]