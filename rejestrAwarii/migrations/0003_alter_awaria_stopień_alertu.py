# Generated by Django 4.1.3 on 2023-08-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rejestrAwarii', '0002_rename_opis_userki_awaria_opis_usterki_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awaria',
            name='stopień_alertu',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=50),
        ),
    ]
