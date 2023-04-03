# Generated by Django 4.1.7 on 2023-04-02 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_condition_file_mara_filed_profil_result_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='mara_marc_for_MS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.TextField(max_length=200)),
                ('designation_article', models.TextField(max_length=200)),
                ('texte_article', models.TextField(max_length=200)),
                ('grpe_march', models.TextField(max_length=200)),
                ('ctrPr', models.TextField(max_length=200)),
                ('typ_app', models.CharField(max_length=1)),
                ('tyAr', models.TextField(max_length=200)),
                ('tL', models.TextField(max_length=200)),
                ('gest', models.TextField(max_length=200)),
                ('di', models.TextField(max_length=200)),
                ('gAc', models.TextField(max_length=200)),
                ('profil', models.TextField(max_length=200)),
                ('prPiAt', models.TextField(max_length=200)),
                ('cree_par', models.TextField(max_length=200)),
                ('langue', models.TextField(max_length=200)),
                ('chant', models.TextField(max_length=200)),
                ('tyP', models.TextField(max_length=200)),
                ('dv', models.TextField(max_length=200)),
                ('gML', models.TextField(max_length=200)),
                ('grPl', models.TextField(max_length=200)),
                ('unP', models.TextField(max_length=200)),
                ('aS', models.IntegerField()),
                ('tCy', models.IntegerField()),
                ('dFI', models.IntegerField()),
                ('dPr', models.IntegerField()),
                ('horiz', models.IntegerField()),
                ('mP', models.IntegerField()),
                ('r', models.IntegerField()),
                ('div', models.IntegerField()),
                ('iC', models.IntegerField()),
                ('stock_securite', models.IntegerField()),
                ('tRe', models.IntegerField()),
                ('gcha', models.IntegerField()),
                ('gS', models.IntegerField()),
                ('int_ajust_amont', models.IntegerField()),
                ('int_ajust_aval', models.IntegerField()),
                ('mode_de_comparaison_des_besoin', models.IntegerField()),
                ('taille_lot_mx', models.IntegerField()),
                ('stock_maximum', models.IntegerField()),
                ('delai_sec', models.IntegerField()),
                ('poids_net', models.IntegerField()),
                ('taille_de_lot_du_CCR', models.IntegerField()),
                ('poids_brut', models.IntegerField()),
                ('mgApp', models.DateField()),
                ('mag', models.DateField()),
                ('cree_le_date', models.DateField()),
                ('aBC', models.CharField(max_length=1)),
                ('uQ', models.CharField(max_length=1)),
                ('lot_fixe', models.BooleanField(default=False)),
                ('taille_l_min', models.BooleanField(default=False)),
                ('val_arrondie', models.BooleanField(default=False)),
                ('ctrl_destinataire', models.CharField(blank=True, max_length=100, null=True)),
                ('article_rempl', models.CharField(blank=True, max_length=100, null=True)),
                ('elément_de_OTP', models.CharField(blank=True, max_length=100, null=True)),
                ('pas_de_CCR', models.CharField(blank=True, max_length=100, null=True)),
                ('rebut', models.FloatField()),
                ('nAl', models.CharField(blank=True, max_length=255, null=True)),
                ('aAppr_déf', models.CharField(blank=True, max_length=255, null=True)),
                ('grpA', models.CharField(blank=True, max_length=255, null=True)),
                ('code_pilotage', models.CharField(blank=True, max_length=255, null=True)),
                ('hiérarch_produits', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='File_mara',
        ),
        migrations.AlterField(
            model_name='condition',
            name='value',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profil',
            name='comment',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='result',
            name='value',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='rule',
            name='comment',
            field=models.TextField(max_length=200),
        ),
    ]
