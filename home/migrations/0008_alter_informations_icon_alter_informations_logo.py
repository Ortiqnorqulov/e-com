# Generated by Django 4.0.2 on 2022-03-01 20:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220301_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informations',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/Info', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg'])]),
        ),
        migrations.AlterField(
            model_name='informations',
            name='logo',
            field=models.ImageField(blank=True, upload_to='images/Info', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg'])]),
        ),
    ]
