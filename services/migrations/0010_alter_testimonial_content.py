# Generated by Django 4.2.4 on 2023-09-07 09:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0009_alter_testimonial_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Testimonio'),
        ),
    ]
