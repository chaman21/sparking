# Generated by Django 3.1.6 on 2021-09-11 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0002_customer_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
