# Generated by Django 4.2.13 on 2024-05-27 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0019_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chargepointextra',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='chargepointextra',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='chargepointextra',
            name='user',
        ),
        migrations.AddField(
            model_name='chargepointextra',
            name='model',
            field=models.CharField(default='DefaultModel', max_length=50),
        ),
        migrations.AddField(
            model_name='chargepointextra',
            name='serial',
            field=models.CharField(default='DefaultSerial', max_length=50),
        ),
        migrations.AddField(
            model_name='chargepointextra',
            name='station',
            field=models.CharField(default='DefaultStation', max_length=100),
        ),
        migrations.AlterField(
            model_name='chargepointextra',
            name='joindate',
            field=models.DateField(default='2024-01-01'),
        ),
    ]
