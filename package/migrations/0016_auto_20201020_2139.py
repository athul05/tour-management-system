# Generated by Django 3.1.2 on 2020-10-20 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0015_auto_20201020_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='package_prize',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='place',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]