from io import StringIO


from django.shortcuts import get_object_or_404, redirect






import pandas as pd

from django.shortcuts import render, redirect 
from django.contrib import messages
import pandas as pd
import psycopg2

from .models import Filed
from datetime import datetime
from .models import mara_marc_for_MS
from .models import Rule
from django.urls import reverse
from django.contrib import messages
from .models import Rule
from .forms import RuleForm

# Données importées
dc = None
 
def home(request):
    return render(request,'home\index.html')


def import_fil(request):
   global dc
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

         #convert an object to a string
         string = str(file)
         mot_a_supprimer = ".xlsx"
         name = string.replace(mot_a_supprimer, "")
        
         
        
         return render(request,'import_file/file.html',{'fichiers_importes': fichiers_importes , 'name':name })
   else:
      return render(request,'import_file/file.html',{'messages' :"Please upload a file!!"})





         
def import_Excel(file,conn):
    global dc

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
   







def delete_file(request, pk):
    global dc
    file = get_object_or_404(mara_marc_for_MS, pk=pk)
    if request.method == 'POST':
        file.delete()
        return redirect('import_fil')
    return render(request,'import_file/file.html')





#def file_detail(request):
 #   global dc
    
 #   if dc is None:
 #     return "Aucune donnée importée."

#      #Conversion des données en une liste de dictionnaires
#    records = dc.to_dict(orient='records')
#    return render(request,'import_file/file_detail.html',{'records':records})
    

import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render

def file_detail(request):
    # Chemin vers le fichier Excel
    fichier_excel = 'C:/Users/HP/Documents/PFE/msenv/ms/mara_marc_for_MS.xlsx'

    try:
        # Charger le fichier Excel
        df = pd.read_excel(fichier_excel)

        # Convertir le DataFrame en HTML
        html_table = df.to_html()  

        # Rendre le template avec le contenu du fichier Excel
        return render(request, 'import_file/file_detail.html', {'html_table': html_table})

    except Exception as e:
        # Gérer les erreurs lors du chargement du fichier Excel
        message_erreur = f"Une erreur s'est produite : {str(e)}"
        return HttpResponse(message_erreur)


def rule_list(request):
    rules = Rule.objects.all()
    return render(request,'rules/list_rule.html', {'rules': rules})


def rule_detail(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    return render(request, 'rules/rule_detail.html', {'rule': rule})



def rule_create(request):
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            rule = form.save(commit=False)
            rule.created_by = request.user
            rule.updated_by = request.user
            rule.save()
            return redirect('rule_detail', pk=rule.pk)
    else:
        form = RuleForm()
    return render(request, 'rules/rule_form.html', {'form': form})



from django.contrib.auth.decorators import login_required

@login_required
def rule_update(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    if request.method == 'POST':
        form = RuleForm(request.POST, instance=rule)
        if form.is_valid():
            rule = form.save(commit=False)
            rule.updated_by = request.user.username  # Utiliser le nom d'utilisateur
            rule.save()
            return redirect('rule_detail', pk=rule.pk)
    else:
        form = RuleForm(instance=rule)
    return render(request, 'rules/rule_form.html', {'form': form})



def rule_delete(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    if request.method == 'POST':
        rule.delete()
        return redirect('rule_list')
    return render(request, 'rules/rule_confirm_delete.html', {'rule': rule})








def test(request):
    return render(request,'home\index.html',{'name':'MSS'})