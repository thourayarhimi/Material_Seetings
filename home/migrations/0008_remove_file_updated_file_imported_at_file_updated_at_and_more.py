# Generated by Django 4.1.7 on 2023-09-08 17:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_date_rute_imported_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='updated',
        ),
        migrations.AddField(
            model_name='file',
            name='imported_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='file',
            name='updated_by',
            field=models.CharField(default=' Rhimi Thouraya', max_length=30),
        ),
        migrations.AlterField(
            model_name='file',
            name='imported_by',
            field=models.CharField(default=' Rhimi Thouraya', max_length=50),
        ),
    ]
