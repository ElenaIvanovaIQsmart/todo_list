# Generated by Django 4.2 on 2023-05-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecomleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
