# Generated by Django 4.1.7 on 2023-06-17 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='restored_by',
            field=models.CharField(default='Thouraya Rhimi  ', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='filed',
            name='restored_by',
            field=models.CharField(default='Thouraya Rhimi  ', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mara_marc_for_ms',
            name='restored_by',
            field=models.CharField(default='Thouraya Rhimi  ', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profil',
            name='restored_by',
            field=models.CharField(default='Thouraya Rhimi  ', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='restored_by',
            field=models.CharField(default='Thouraya Rhimi  ', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='restored_by',
            field=models.CharField(default='Thouraya Rhimi  ', max_length=30, null=True),
        ),
    ]
