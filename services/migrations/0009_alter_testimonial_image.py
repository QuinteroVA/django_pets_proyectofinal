# Generated by Django 4.2.4 on 2023-09-05 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_alter_testimonial_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(upload_to='services', verbose_name='imagen'),
        ),
    ]
