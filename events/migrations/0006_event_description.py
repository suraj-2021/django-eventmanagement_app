# Generated by Django 4.2.5 on 2023-09-20 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_rename_pymanager_event_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
