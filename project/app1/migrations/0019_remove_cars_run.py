# Generated by Django 3.2.10 on 2023-04-22 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_alter_cars_run'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cars',
            name='run',
        ),
    ]
