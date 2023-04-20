from io import StringIO
import os





import pandas as pd

from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
import psycopg2


from datetime import datetime
from .models import mara_marc_for_MS

from django.urls import reverse
from django.contrib import messages





def home(request):
    return render(request,'home\index.html')
def products(request):
  category = request.GET.get('category', 'All')
  if category == 'All':
    products = Product.objects.all()
  else:
    products = Product.objects.filter(category=category)
  return render(request, 'products.html', {'products': products})

def import_fil(request):
   if request.method == 'POST' and  request.FILES:
      
      
         file = request.FILES['file']
         #  Connexion à la base de données
         conn = psycopg2.connect(
               host="localhost",
               database="ms_db",
               user="postgres",
               password="123456789",
               port="5432",
            )
         import_Excel(file,conn)
         messages.success(request,' importées avec succès.')
         # create queryset containing only last record
         last_imported_file = mara_marc_for_MS.objects.latest('created_at')
         fichiers_importes = [last_imported_file]
         mes_donnees = mara_marc_for_MS.objects.all()
         total_fichiers = len(mes_donnees)
         
        
         
        
         return render(request,'import_file/file.html',{'fichiers_importes': fichiers_importes, 'total_fichiers': total_fichiers})
   else:
      return render(request,'import_file/file.html',{'messages' :"Please upload a file!!"})





         
def import_Excel(file,conn):

    #read file with pandas

    dc=pd.read_excel(file)

    #insert informations into file

    dc.insert(0,'created_at',datetime.now())

    dc.insert(1,'updated_at',datetime.now())

    dc.insert(2,'created_by','thouraya')

    dc.insert(3,'updated_by','thouraya')

    dc.insert(4,'is_deleted',False)

    dc.insert(5,'deleted_by','thouraya')

    dc.insert(6,'deleted_at',datetime.now())

    dc.insert(7,'restored_at',datetime.now())

    dc.insert(8,'restored_by','thouraya')

    

 

    # Using the StringIO method to set

    # as file object

    # print(dc.head(10))

    Excel= StringIO()

    #convert file to csv

    Excel.write(dc.to_csv(index=None , header=None))

    # This will make the cursor at index 0

    Excel.seek(0)

    with conn.cursor() as c:

        c.copy_from(

            file=Excel,

            #file name in DB

            table="home_mara_marc_for_ms",

            columns=[
               'created_at',
               'updated_at',
               'created_by',
               'updated_by',
               'is_deleted',
               'deleted_by',
               'deleted_at',
               'restored_at',
               'restored_by',
               'article',
               'designation_article',
               'texte_article',
               'grpe_march',
               'div',
               'ctrPr',
               'typ_app',
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
               'mag' ,
               'tL',
               'lot_fixe',
               'uQ',
               'stock_securite',
               'uQ_1',
               'tRe',
               'gest',
               'di',
               'rebut',
               'gAc',
               'profil', 
               'prPiAt', 
               'cree_par',
               'langue',
               'cree_le_date',  
               'gcha', 
               'gS', 
               'mode_de_comparaison_des_besoin',
               'int_ajust_amont' ,
               'int_ajust_aval',  
               'taille_l_min',
               'uQ_2',
               'val_arrondie',  
               'uQ_3',
               'taille_lot_mx',
               'uQ_4',
               'stock_maximum',
               'uQ_5',
               'chant',
               'tyP',
               'delai_sec',
               'delai_sec_1',
               'ctrl_destinataire',
               'article_rempl',
               'dv',
               'gML',
               'grPl',
               'aBC',
               'uQ_6',
               'elément_de_OTP', 
               'grpA',   
               'code_pilotage',
               'hierarch_produits', 
               'poids_brut',  
               'unP',
               'poids_net' ,
               'unP_1',
               'pas_de_CCR' ,
               'taille_de_lot_du_CCR',
               'uQ_7',
             ],
            
            null="",

            sep=",",
            )

    conn.commit()  
   







  
def test(request):
    return render(request,'home\index.html',{'name':'MSS'})