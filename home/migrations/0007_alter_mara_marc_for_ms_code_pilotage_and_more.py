# Generated by Django 4.1.7 on 2023-04-07 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_mara_marc_for_ms_gs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mara_marc_for_ms',
            name='code_pilotage',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mara_marc_for_ms',
            name='delai_sec',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mara_marc_for_ms',
            name='delai_sec_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mara_marc_for_ms',
            name='elément_de_OTP',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mara_marc_for_ms',
            name='grpA',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mara_marc_for_ms',
            name='hierarch_produits',
            field=models.TextField(blank=True, null=True),
        ),
    ]
