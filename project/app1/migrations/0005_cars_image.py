# Generated by Django 3.2.10 on 2023-04-14 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20230414_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]