# Generated by Django 4.1.7 on 2023-09-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_todo_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
