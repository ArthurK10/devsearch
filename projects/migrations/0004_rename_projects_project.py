# Generated by Django 4.2.7 on 2024-01-07 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_rename_project_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
