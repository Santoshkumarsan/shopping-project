# Generated by Django 3.0 on 2020-12-05 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0013_auto_20201205_1129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('slug', 'parent')},
        ),
    ]
