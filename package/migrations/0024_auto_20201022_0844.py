# Generated by Django 3.1.2 on 2020-10-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0023_enquirie_urgent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquirie',
            name='urgent',
            field=models.CharField(max_length=10),
        ),
    ]
