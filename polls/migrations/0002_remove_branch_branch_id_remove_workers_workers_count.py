# Generated by Django 4.2.5 on 2023-09-06 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='branch_id',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='workers_count',
        ),
    ]