# Generated by Django 3.1.6 on 2021-02-19 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210219_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Completed_Date',
            field=models.DateField(blank=True),
        ),
    ]
