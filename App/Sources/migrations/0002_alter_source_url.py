# Generated by Django 4.2 on 2023-05-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(blank=True, default=''),
        ),
    ]