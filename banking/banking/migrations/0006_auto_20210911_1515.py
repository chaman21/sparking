# Generated by Django 3.1.6 on 2021-09-11 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0005_auto_20210911_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trans',
            name='email',
        ),
        migrations.RemoveField(
            model_name='trans',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='trans',
            name='name',
        ),
    ]
