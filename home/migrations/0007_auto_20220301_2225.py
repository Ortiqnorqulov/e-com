# Generated by Django 3.2.10 on 2022-03-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20220228_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informations',
            name='image',
        ),
        migrations.AlterField(
            model_name='informations',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/Info'),
        ),
        migrations.AlterField(
            model_name='informations',
            name='logo',
            field=models.ImageField(blank=True, upload_to='images/Info'),
        ),
    ]
