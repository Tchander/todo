# Generated by Django 3.2.4 on 2021-06-10 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='todos',
            new_name='category',
        ),
    ]