# Generated by Django 4.2 on 2023-05-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sources', '0002_alter_source_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='file',
            field=models.FileField(blank=True, null=True, unique=True, upload_to='Sources/'),
        ),
    ]
