# Generated by Django 4.1.1 on 2024-05-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writting_checker', '0002_userwrittings_public_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwrittings',
            name='task',
            field=models.CharField(max_length=500),
        ),
    ]