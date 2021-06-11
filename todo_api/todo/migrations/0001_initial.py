# Generated by Django 3.2.4 on 2021-06-10 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, default=None, max_length=100, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default=None, max_length=200, verbose_name='Text')),
                ('isCompleted', models.BooleanField(default=False)),
                ('todos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.todocategory')),
            ],
        ),
    ]
