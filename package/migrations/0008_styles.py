# Generated by Django 3.1.2 on 2020-10-19 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0007_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='styles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]