# Generated by Django 4.2.5 on 2023-09-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclubuser',
            name='first_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='last_name',
            field=models.CharField(max_length=120),
        ),
    ]