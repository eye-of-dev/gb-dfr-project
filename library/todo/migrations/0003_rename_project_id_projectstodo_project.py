# Generated by Django 3.2.7 on 2021-09-27 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20210927_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectstodo',
            old_name='project_id',
            new_name='project',
        ),
    ]
