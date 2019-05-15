# Generated by Django 2.2.1 on 2019-05-14 01:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('haitiApp', '0006_auto_20190513_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_image',
            name='uploadedAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='productDescription',
            field=models.TextField(verbose_name='productDescription'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productName',
            field=models.CharField(max_length=250, unique=True, verbose_name='productName'),
        ),
        migrations.AlterField(
            model_name='product_image',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='products/productImages/', verbose_name='img'),
        ),
    ]
