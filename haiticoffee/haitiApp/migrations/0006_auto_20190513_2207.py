# Generated by Django 2.2.1 on 2019-05-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haitiApp', '0005_auto_20190513_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(default='United States', max_length=250, verbose_name='country'),
        ),
    ]
