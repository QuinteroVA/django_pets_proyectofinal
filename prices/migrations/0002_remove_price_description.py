# Generated by Django 4.2.4 on 2023-09-05 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='description',
        ),
    ]