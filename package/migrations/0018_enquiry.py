# Generated by Django 3.1.2 on 2020-10-21 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0017_auto_20201021_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('messsage', models.TextField()),
            ],
        ),
    ]