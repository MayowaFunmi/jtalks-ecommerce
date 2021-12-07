# Generated by Django 3.2.9 on 2021-12-06 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0008_alter_coursereview_review_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLibrary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses', models.ManyToManyField(blank=True, to='courses.Courses')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='library', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserLibraries',
            },
        ),
    ]
