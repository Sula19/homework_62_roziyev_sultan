# Generated by Django 4.1.7 on 2023-03-20 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_task_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='author',
        ),
    ]
