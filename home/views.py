from django.shortcuts import render
import pandas as pd
import psycopg2
import openpyxl
from django.db import connection
from .models import mara_marc_for_MS
from django.http import HttpResponse


def home(request):
    return render(request,'home\index.html')

def import_excel(request):
    
    if request.method == 'POST':
    
      # establish connection
      conn = psycopg2.connect(
        host="localhost",
        database="ms_db",
        user="postgres",
        password="123456789"
      )
      # create a cursor
      cur = conn.cursor()
      # open the file
      
      with open('mara_marc_for_MS.xlsx','r',encoding="utf8") as f:
      # skip the header line if it exists
       next(f)
      # copy the contents of the file into the database
       cur.copy_from(f,'mara_marc_for_MS', sep=',', columns=('article', 
                                                             'designation_article ',
                                                             'texte_article',
                                                             'grpe_march',
                                                             'div',
                                                             'ctrPr',
                                                             'typ_app' ,
                                                             'aS',
                                                             'tCy',
                                                             'dFI',
                                                             'dPr',
                                                             'horiz',
                                                             'mP',
                                                             'r',
                                                             'tyAr',
                                                             'nAl',
                                                             'iC',
                                                             'aAppr_def',
                                                             'mgApp',
                                                             'mag',
                                                             'tL',
                                                             'lot_fixe' 
                                                             ,'uQ',
                                                             'stock_securite',
                                                             'uQ_1',
                                                             'tRe' ,
                                                             'gest',
                                                             'di',
                                                             'rebut' ,
                                                             'gAc' ,
                                                             'profil' ,
                                                             'prPiAt' ,
                                                             'cree_par',
                                                             'langue',
                                                             'cree_le_date',
                                                             'gcha',
                                                             'gS',
                                                             'mode_de_comparaison_des_besoin',
                                                             'int_ajust_amont',
                                                             'int_ajust_aval',
                                                             'taille_l_minu',
                                                             'uQ_2',
                                                             'val_arrondie ',
                                                             'uQ_3',
                                                             'taille_lot_mxu',
                                                             'uQ_4',
                                                             'stock_maximumu',
                                                             'uQ_5',
                                                             'chant',
                                                             'tyP',
                                                             'delai_sec ',
                                                             'delai_sec_1',
                                                             'ctrl_destinataire' ,
                                                             'article_rempl',
                                                             'dv',
                                                             'gML',
                                                             'grPl',
                                                             'aBC',
                                                             'uQ_6',
                                                             'elément_de_OTP',
                                                             'grpA',
                                                             'code_pilotage',
                                                             'hiérarch_produits',
                                                             'poids_brut',
                                                             'unP',
                                                             'poids_net',
                                                             'unP',
                                                             'pas_de_CCR',
                                                             'taille_de_lot_du_CCR' ,
                                                             'uQ_7'  ))
    
      # commit the changes
      conn.commit()

      # close the cursor and the connection
      cur.close()
      conn.close()

      # Traitez les données ici
    return render(request, 'home\import_excel.html', {'message': 'Importation réussie!'})
    return render(request, 'home\import_excel.html')



def test(request):
    return render(request,'home\index.html',{'name':'MSS'})