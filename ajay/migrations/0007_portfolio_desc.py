# Generated by Django 4.1.2 on 2022-10-19 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajay', '0006_remove_home_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='desc',
            field=models.TextField(blank=True),
        ),
    ]
