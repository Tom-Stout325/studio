# Generated by Django 4.2.4 on 2023-08-07 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_number',
            old_name='client_number',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='session_number',
            old_name='Session_number',
            new_name='id',
        ),
    ]