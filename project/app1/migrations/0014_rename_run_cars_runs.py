# Generated by Django 3.2.10 on 2023-04-21 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_auto_20230421_1648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='run',
            new_name='runs',
        ),
    ]
