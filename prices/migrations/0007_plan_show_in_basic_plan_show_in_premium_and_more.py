# Generated by Django 4.2.4 on 2023-09-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0006_alter_plan_icon_class_alter_plan_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='show_in_basic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plan',
            name='show_in_premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='plan',
            name='show_in_standard',
            field=models.BooleanField(default=False),
        ),
    ]