# Generated by Django 3.2.7 on 2023-11-25 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engross_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userformdata',
            name='age',
        ),
        migrations.RemoveField(
            model_name='userformdata',
            name='state',
        ),
        migrations.AlterField(
            model_name='userformdata',
            name='college',
            field=models.CharField(max_length=250),
        ),
    ]
