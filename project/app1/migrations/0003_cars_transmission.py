# Generated by Django 3.2.10 on 2023-04-14 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_cars_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='transmission',
            field=models.CharField(choices=[('a', 'Automatic'), ('m', 'Mechanic')], default='a', max_length=2),
        ),
    ]
