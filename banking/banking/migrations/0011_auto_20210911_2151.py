# Generated by Django 3.1.6 on 2021-09-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0010_auto_20210911_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trans',
            name='email',
            field=models.CharField(max_length=60),
        ),
    ]
