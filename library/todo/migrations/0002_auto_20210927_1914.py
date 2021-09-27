# Generated by Django 3.2.7 on 2021-09-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Проект', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterModelOptions(
            name='projectstodo',
            options={'verbose_name': 'Заметка', 'verbose_name_plural': 'Заметки'},
        ),
        migrations.AlterField(
            model_name='projects',
            name='link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Ссылка'),
        ),
    ]
