# Generated by Django 3.2.9 on 2021-12-11 11:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_userlibrary_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
