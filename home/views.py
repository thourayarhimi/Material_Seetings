from django.shortcuts import render, redirect
from django.contrib import messages
import pandas as pd
import os
import numpy
import psycopg2
from django.views.decorators.csrf import csrf_exempt

from .models import mara_marc_for_MS





def home(request):
    return render(request,'home\index.html')
 

# def import_fil(request):
#    if request.method == 'POST':
#       file = request.FILES['file']   
#       df = pd.read_excel(file)
#       df = df.where(pd.notnull(df), None)
#       objs = [
#         mara_marc_for_MS(
#             article=row['Article'],
#             designation_article=row['Désignation article'], 
#             texte_article=row['Texte Article'],
#             grpe_march=row['Grpe march.'],
#             div=row['Div.'],
#             ctrPr=row['CtrPr'],
#             typ_app=row['Typ.App.'],
#             aS=row['A.S'],
#             tCy=row['TCy'],
#             dFI=row['DFI'],
#             dPr=row['DPr'],
#             horiz=row['Horiz'],
#             mP=row['MP'],
#             r=row['R'],
#             tyAr=row['TyAr'],
#             nAl=row['NAl'],
#             iC=row['I/C'],
#             aAppr_def=row['AAppr/déf'],
#             mgApp=row['MgApp'],
#             mag=row['Mag.'],
#             tL=row['TL'],
#             lot_fixe=row['Lot fixe'],
#             uQ=row['UQ'],
#             stock_securite  =row['Stock sécurité'],
#             uQ_1=row['UQ'],
#             tRe=row['TRé'],
#             gest=row['Gest.'],
#             di=row['Di'],
#             rebut=row['Rebut'],
#             gAc=row['GAc'],
#             profil=row['Profil'],
#             prPiAt=row['PrPiAt'],
#             cree_par=row['Créé par'],
#             langue=row['Langue'],
#             cree_le_date=row['Créé le'], 
#             gcha=row['GCha'],
#             gS=row['GS'],
#             mode_de_comparaison_des_besoin=row['Mode de comparaison des besoin'],
#             int_ajust_amont=row['Int.ajust.amont'],
#             int_ajust_aval=row['Int.ajust.aval'],
#             taille_l_min=row['Taille l.min'],
#             uQ_2=row['UQ'],
#             val_arrondie=row['Val.arrondie'],
#             uQ_3=row['UQ'],
#             taille_lot_mx=row['Taille lot mx'],
#             uQ_4=row['UQ'],
#             stock_maximum=row['Stock maximum'],
#             uQ_5=row['UQ'],
#             chant=row['Chant'],
#             tyP=row['TyP'],
#             delai_sec=row['Délai séc.'],
#             delai_sec_1=row['Délai séc.'],
#             ctrl_destinataire =row['Ctrl destinataire'],
#             article_rempl=row['Article rempl.'],
#             dv=row['Dv'],
#             gML=row['GML'],
#             grPl=row['GrPl'],
#             aBC=row['ABC'],
#             uQ_6=row['UQ'],
#             elément_de_OTP=row['Element d OTP'],
#             grpA=row['GrpA'],
#             code_pilotage=row['Code pilotage'],
#             hierarch_produits=row['Hiérarch.produits'],
#             poids_brut=row['Poids brut'], 
#             unP=row['UnP'],
#             poids_net=row['Poids net'],
#             unP_1=row['UnP'],
#             pas_de_CCR=row['pas de CCR'],
#             taille_de_lot_du_CCR=row['Taille de lot du CCR'],
#             uQ_7=row['UQ']
#            )
#            for index, row in df.iterrows()
#         ]
#       mara_marc_for_MS.objects.bulk_create(objs)
       
          
#       return render(request,'import_file/file.html',{'messages' :'import file is successful'})
  
#    return render(request,'import_file/file.html')
  
@csrf_exempt
def import_fil(request):
   if request.method == 'POST':
      
         file = request.FILES['file']
       
         df = pd.read_excel(file)
         
         try:
  
            #  Connexion à la base de données
            conn = psycopg2.connect(
                  host="localhost",
                  database="ms_db",
                  user="postgres",
                  password="123456789",
                  port="5432",
               )
            cur = conn.cursor()
            print("11")

            records = df.to_records(index=False)
            cur.executemany("INSERT INTO home_mara_marc_for_ms (Article,Désignation article,Texte Article,Grpe march.,Div. ,CtrPr ,Typ.App.,A.S,TCy,DFI,DPr,Horiz ,MP,r,TyAr,NAl,I/C,AAppr/def,MgApp,Mag,TL,Lot fixe' ,UQ,Stock sécurité,UQ,TRé ,Gest.,Di,Rebut,GAc,Profil,PrPiAt,Créé par,Langue,Créé le,GCha,GS,Mode de comparaison des besoin,Int.ajust.amont,Int.ajust.aval,Taille l.min,UQ,Val.arrondie,UQ,Taille lot mx,UQ,Stock maximum,UQ,Chant,TyP,Délai séc.,Délai séc.,Ctrl destinataire,Article rempl.,Dv,GML,GrPl,ABC,UQ,Element d OTP,GrpA,Code pilotage,Hiérarch.produits,Poids brut,UnP,Poids net,UnP,pas de CCR,Taille de lot du CCR,UQ)VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", records)
            conn.commit()
            cur.close()
         except(Exception, psycopg2.DatabaseError) as error:
          print(error)
          
        
        
    
         finally:
           if conn is not None:
              conn.close()
              
              
         return render(request,'import_file/file.html',{'messages' :'import file is successful'})
  
   return render(request,'import_file/file.html')

  
def test(request):
    return render(request,'home\index.html',{'name':'MSS'})