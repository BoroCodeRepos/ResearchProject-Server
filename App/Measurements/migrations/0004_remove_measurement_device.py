# Generated by Django 4.2 on 2023-05-14 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Measurements', '0003_alter_measurement_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='device',
        ),
    ]
