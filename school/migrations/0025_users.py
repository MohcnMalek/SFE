# Generated by Django 4.2.13 on 2024-05-30 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0024_client_energy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(default='', max_length=255, unique=True)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('functions', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
