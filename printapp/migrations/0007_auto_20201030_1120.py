# Generated by Django 3.0 on 2020-10-30 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0006_auto_20201027_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='fullname',
            field=models.CharField(default='', max_length=64),
        ),
    ]