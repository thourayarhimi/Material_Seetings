# Generated by Django 4.1.7 on 2023-12-14 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_chatmessage_imported_at_chatmessage_imported_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='imported_at',
        ),
        migrations.RemoveField(
            model_name='condition',
            name='imported_by',
        ),
        migrations.RemoveField(
            model_name='condition',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='condition',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='rute',
            name='imported_at',
        ),
        migrations.RemoveField(
            model_name='rute',
            name='imported_by',
        ),
        migrations.RemoveField(
            model_name='rute',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='rute',
            name='updated_by',
        ),
    ]