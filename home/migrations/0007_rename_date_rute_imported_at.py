# Generated by Django 4.1.7 on 2023-09-08 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_rute_deleted_at_remove_rute_deleted_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rute',
            old_name='date',
            new_name='imported_at',
        ),
    ]