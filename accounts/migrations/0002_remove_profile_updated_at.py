# Generated by Django 4.1.7 on 2023-04-11 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='updated_at',
        ),
    ]