# Generated by Django 3.1.2 on 2020-10-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0008_styles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='styles',
        ),
        migrations.AddField(
            model_name='destination',
            name='style',
            field=models.CharField(default=1, max_length=10, verbose_name='style1-style6'),
            preserve_default=False,
        ),
    ]
