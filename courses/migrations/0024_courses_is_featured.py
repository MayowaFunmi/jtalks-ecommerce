# Generated by Django 3.2.9 on 2021-12-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_auto_20211213_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
