# Generated by Django 4.2 on 2023-04-12 08:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('INF', 'Information'), ('WAR', 'Warning'), ('ERR', 'Error')], default='INF', max_length=3)),
                ('text', models.CharField(max_length=255)),
                ('registration_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
