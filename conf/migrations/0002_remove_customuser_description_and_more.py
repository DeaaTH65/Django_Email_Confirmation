# Generated by Django 4.2.6 on 2023-11-26 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='description',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='status',
        ),
    ]
