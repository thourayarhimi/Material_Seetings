
import io
from django.urls import reverse
from django.shortcuts import get_object_or_404, render,redirect
from .models import FileMs
from .models import File,condition
import pandas as pd 
import psycopg2 
from django.contrib.auth.models import User


from django.shortcuts import render, get_object_or_404, redirect
from .models import rute,resulta,lm
from .forms import RuleForm




# Create your views here.


    
def home(request):
    return render(request,'home\index.html')


def file(request):
    context = {}
    file=File.objects.all()
    context['data']=file
  
    return render(request,'import_file/file.html',context )




def upload(request):
    context = {}
    template = "import_file/upload_file.html"


    if request.method == "GET":

        
        return render(request , 'import_file/upload_file.html', context)
    
    
    if request.method== 'POST':
        
        file=request.FILES['my_file']
        



        
        
        conn=psycopg2.connect(host='localhost',dbname='MS_db',user='postgres',password='123456789',port='5432')
        import_ms_file(request,file,conn) 
        file=File.objects.all()
        context['data']=file       
      
    return render(request , 'import_file/file.html' , context)




def import_ms_file (request,file,conn):
    #read file pandas
    connn=psycopg2.connect(host='localhost',dbname='MS_db',user='postgres',password='123456789',port='5432')
    username = request.user
    user ="thouraya"
    print("thouuuuu")
    print(username)
    ll= File.objects.create(name=file,imported_by= username )
    ll.save()
    dc=pd.read_excel(file)
    f=dc
    filee=pd.DataFrame(f)
    # Cela spécifie que vous souhaitez sélectionner toutes les lignes (:) de la colonne 'file_id'.

    filee.loc[:,'file_id']=ll.id
    
    # Using the StringIO method to set

    # as file object
    
    msfilee=io.StringIO()
    #convert file to csv
    msfilee.write(filee.to_csv(index=None,header=None))
    # This will make the cursor at index 0
    msfilee.seek(0)
    print(filee)
    print("///////////////////////////////")
    msfilee.seek(0)
    print(msfilee.read())
    msfilee.seek(0)
    with connn.cursor() as c:
            vall=ll.name,
            
            c.copy_from(
           
            file=msfilee,
            #file name in DB
            table= "home_filems",
            
            columns=[
       
       'article',
       'designation_article',
       'text_article',
       'grpe_march',
       'div',
       'ctrpr',
       'typ_app',
       'a_s',
       'tcy',
       'dfi',
       'dpr',
       'horiz',
       'mp',
       'r',
       'tyar',
       'nal',
       'i_c',
       'aappr_def',
       'mgapp',
       'mag',
       'tl',
       'lot_fixe',
       'uq1',
       'stock_securite',
       'uq0',
       'tre',
       'gest',
       'di',    
       'rebut',
       'gac',
       'Profil',
       'prpiAt',
       'cree_par',
       'langue',
       'Cree_le',
       'gcha',
       'gs',
       'mode_de_comparaison_des_besoin',
       'int_ajust_amont',
       'int_ajust_aval',
       'taille_l_min',
       'uq2',
       'val_arrondie',
       'uq3',
       'taille_lot_mx',
       'uq4',
       'stock_maximum',
       'uq5',
       'chant',
       'typ',
       'delai_sec',
       'delai_sec1',
       'ctrl_destinataire',
       'article_rempl',
       'dv',
       'gml',
       'grpl',
       'abc',
       'uq6',
       'element_dOTP',
       'grpa',
       'Code_pilotage',
       'hierarch_produits',
       'poids_brut',
       'unp1',
       'poids_net',
       'unp2',
       'pas_de_ccr',
       'Taille_de_lot_du_CCR',
       'uq7',
       'file_id'
       
       

        ],
        null="",
        sep=",",
        
        

        ),
    
            
             
            
    connn.commit()
    




def delit  (request,id):
    context = {}
    d=FileMs.objects.filter(file_id=id).delete()
    File.objects.filter(id=id).delete()
 
        
    file=File.objects.all()
    context['data']=file

    return render(request,'import_file/file.html',context )
        



#filter 
def filter(request,id):
    context = {}
   
   
    context['id']=id
    

    return render(request,'import_file/filter.html',context )


def getfilter(request,id):
    context = {}
   
    
    context['id']=id
    

    
    d=FileMs.objects.filter(file_id=id)
   
  
    
    

   
    context['id']=id
    

    if request.method== 'POST':
        languages = request.POST.getlist('inlineCheckbox2')
        print("thoura88888888888888888888888888888")
        print(languages)
        print("thoura99999999999999999999999999")
        if(languages):
                
                 
            context['data']=d
               
            context['list']=languages
               
                 
                
        else:
                context['data']=d
   
                context['list']=[
                
                'article',
       'designation_article',
       'text_article',
       'grpe_march',
       'div',
       'ctrpr',
       'typ_app',
       'a_s',
       'tcy',
       'dfi',
       'dpr',
       'horiz',
       'mp',
       'r',
       'tyar',
       'nal',
       'i_c',
       'aappr_def',
       'mgapp',
       'mag',
       'tl',
       'lot_fixe',
       'uq1',
       'stock_securite',
       'uq0',
       'tre',
       'gest',
       'di',    
       'rebut',
       'gac',
       'Profil',
       'prpiAt',
       'cree_par',
       'langue',
       'Cree_le',
       'gcha',
       'gs',
       'mode_de_comparaison_des_besoin',
       'int_ajust_amont',
       'int_ajust_aval',
       'taille_l_min',
       'uq2',
       'val_arrondie',
       'uq3',
       'taille_lot_mx',
       'uq4',
       'stock_maximum',
       'uq5',
       'chant',
       'typ',
       'delai_sec',
       'delai_sec1',
       'ctrl_destinataire',
       'article_rempl',
       'dv',
       'gml',
       'grpl',
       'abc',
       'uq6',
       'element_dOTP',
       'grpa',
       'Code_pilotage',
       'hierarch_produits',
       'poids_brut',
       'unp1',
       'poids_net',
       'unp2',
       'pas_de_ccr',
       'Taille_de_lot_du_CCR',
       'uq7']
                
    
    print  (context['list'])  
    return render(request,'import_file/filter.html',context )






def rule_list(request):
    rules = rute.objects.all()
    return render(request,'rules/list_rule.html', {'rules': rules})


def rule_detail(request, pk):
    #get_object_or_404 est utilisé pour récupérer un objet spécifique 
    #  à partir de la base de données en fonction de sa clé primaire, 
    # et s'il n'est pas trouvé, 
    # il renvoie une réponse HTTP 404 pour indiquer que l'objet n'existe pas.
    rule = get_object_or_404(rute, pk=pk)
    return render(request, 'rules/rule_detail.html', {'rule': rule})



def rule_create(request):
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            # Les données du formulaire sont valides ou non sinon  traiter ici, 
            rule = form.save(commit=False)
            rule.created_by = request.user
            rule.updated_by = request.user
            rule.save()
            return redirect('rule_detail', pk=rule.pk)
    else:
        form = RuleForm()
    return render(request, 'rules/rule_form.html', {'form': form})




def rule_update(request, pk):
    rule = get_object_or_404(rute, pk=pk)
    if request.method == 'POST':
      
        if form.is_valid():
            rule = form.save(commit=False)
            rule.updated_by = request.user  # Utiliser le nom d'utilisateur
            rule.save()
            return redirect('rule_detail', pk=rule.pk)
    else:
        form = RuleForm(instance=rule)
    return render(request, 'rules/rule_form.html', {'form': form})



def rule_delete(request, pk):
    rule = get_object_or_404(rute, pk=pk)
    if request.method == 'POST':
        rule.delete()
        return redirect('rule_list')
    return render(request, 'rules/rule_confirm_delete.html', {'rule': rule})







def list_condition(request):
    context = {}
    
    cc=condition.objects.all() 
    context['data']=cc

    return render(request,'condition/List_condition.html' ,context )



def Condition(request):
    context = {}
    
    cc=condition.objects.all() 
    context['data']=cc

    return render(request,'condition/condition.html' ,context )

def conditionn(request,id):
    context = {}
    r=rute.objects.filter(id=id).get()
    cc=condition.objects.filter(id_rute=r)
   
    context['data']=cc
    if request.method== 'POST':
        field=request.POST['choix']
        co=request.POST['condition']
        c=condition.objects.create(field=field,Con=co,id_rute=r)
        c.save()
    return render(request,'condition/condition.html',context )

def delete_condution(request, pk):
    delet_con = get_object_or_404(condition, pk=pk)
    if request.method == 'POST':
        delet_con.delete()
        return redirect('Condition' )
    return render(request, 'condition/condition.html', {' delet_con': delet_con})

# UPDATE CONDUTION 



def resultas_all (request):
    context = {}
    cc=resulta.objects.all()
    
   
    
    context['data']=cc
    return render(request,'Resulta/resultas.html' ,context )

def resulta_id(request,id):
    context = {}
   
    r=condition.objects.filter(id=id).get()
    cc=resulta.objects.filter(id_condition=r)
    
 
    context['data']=cc

    if request.method== 'POST':
        field=request.POST['choix']
        co=request.POST['condition']
        c=resulta.objects.create(field=field,Res=co,id_condition=r)
        c.save()
    return render(request,'Resulta/resultas.html' ,context )


def resultas_List (request):
    context = {}
    cc=resulta.objects.all()
    
   
    
    context['data']=cc
    return render(request,'Resulta/result_list.html' ,context )





def table(request,id):
    context = {}
  
    N_case_modifier=0
    nu_case=0
    case_non_treter=0
    classs=""
    
    d=FileMs.objects.filter(file_id=id)
   
    condi=lm.objects.filter(id_file=id)
    
    for i in d:
        
        
        if((len(lm.objects.filter(id_file=id,id_ligne=i.pk,field='article').values_list()))>0):
                     i.article=lm.objects.filter(id_file=id,id_ligne=i.pk,field='article').values_list()    
                     
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='designation_article')):
                     i.designation_article=lm.objects.filter(id_file=id,id_ligne=i.pk,field='designation_article').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='text_article')):
                     i.text_article=lm.objects.filter(id_file=id,id_ligne=i.pk,field='text_article').values_list()                          
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='grpe_march')):
                     i.grpe_march=lm.objects.filter(id_file=id,id_ligne=i.pk,field='grpe_march').values_list()                   
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='div')):
                     i.div=lm.objects.filter(id_file=id,id_ligne=i.pk,field='div').values_list() 
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='ctrpr')):
                     i.ctrpr=lm.objects.filter(id_file=id,id_ligne=i.pk,field='ctrpr').values_list()
         
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='typ_app')):
                     i.typ_app=lm.objects.filter(id_file=id,id_ligne=i.pk,field='typ_app').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='a_s')):
                     i.a_s=lm.objects.filter(id_file=id,id_ligne=i.pk,field='a_s').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='tcy')):
                     i.tcy=lm.objects.filter(id_file=id,id_ligne=i.pk,field='tcy').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='dfi')):
                     i.dfi=lm.objects.filter(id_file=id,id_ligne=i.pk,field='dfi').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='dpr')):
                     i.dpr=lm.objects.filter(id_file=id,id_ligne=i.pk,field='dpr').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='horiz')):
                     i.horiz=lm.objects.filter(id_file=id,id_ligne=i.pk,field='horiz').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='mp')):
                     i.mp=lm.objects.filter(id_file=id,id_ligne=i.pk,field='mp').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='r')):
                     i.r=lm.objects.filter(id_file=id,id_ligne=i.pk,field='r').values_list()
                             
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='tyar')):
                     i.tyar=lm.objects.filter(id_file=id,id_ligne=i.pk,field='tyar').values_list()
                             
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='nal')):
                     i.nal=lm.objects.filter(id_file=id,id_ligne=i.pk,field='nal').values_list()
                             
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='i_c')):
                     i.i_c=lm.objects.filter(id_file=id,id_ligne=i.pk,field='i_c').values_list()
                             
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='aappr_def')):
                     i.aappr_def=lm.objects.filter(id_file=id,id_ligne=i.pk,field='aappr_def').values_list()
                             
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='mgapp')):
                     i.mgapp=lm.objects.filter(id_file=id,id_ligne=i.pk,field='mgapp').values_list()
                             
        
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='mag')):
                     i.mag=lm.objects.filter(id_file=id,id_ligne=i.pk,field='mag').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='tl')):
                     i.tl=lm.objects.filter(id_file=id,id_ligne=i.pk,field='tl').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='lot_fixe')):
                     i.lot_fixe=lm.objects.filter(id_file=id,id_ligne=i.pk,field='lot_fixe').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq1')):
                     i.uq1=lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq1').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='stock_securite')):
                     i.stock_securite=lm.objects.filter(id_file=id,id_ligne=i.pk,field='stock_securite').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq0')):
                     i.uq0=lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq0').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='tre')):
                     i.tre=lm.objects.filter(id_file=id,id_ligne=i.pk,field='tre').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='gest')):
                     i.gest=lm.objects.filter(id_file=id,id_ligne=i.pk,field='gest').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='di')):
                     i.di=lm.objects.filter(id_file=id,id_ligne=i.pk,field='di').values_list()
        




        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='rebut')):
                     i.rebut=lm.objects.filter(id_file=id,id_ligne=i.pk,field='rebut').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='gac')):
                     i.gac=lm.objects.filter(id_file=id,id_ligne=i.pk,field='gac').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='Profil')):
                     i.Profil=lm.objects.filter(id_file=id,id_ligne=i.pk,field='Profil').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='prpiAt')):
                     i.prpiAt=lm.objects.filter(id_file=id,id_ligne=i.pk,field='prpiAt').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='cree_par')):
                     i.cree_par=lm.objects.filter(id_file=id,id_ligne=i.pk,field='cree_par').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='langue')):
                     i.langue=lm.objects.filter(id_file=id,id_ligne=i.pk,field='langue').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='Cree_le')):
                     i.Cree_le=lm.objects.filter(id_file=id,id_ligne=i.pk,field='Cree_le').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='gcha')):
                     i.gcha=lm.objects.filter(id_file=id,id_ligne=i.pk,field='gcha').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='gs')):
                     i.gs=lm.objects.filter(id_file=id,id_ligne=i.pk,field='gs').values_list()
        








        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='mode_de_comparaison_des_besoin')):
                     i.mode_de_comparaison_des_besoin=lm.objects.filter(id_file=id,id_ligne=i.pk,field='mode_de_comparaison_des_besoin').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='int_ajust_amont')):
                     i.int_ajust_amont=lm.objects.filter(id_file=id,id_ligne=i.pk,field='int_ajust_amont').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='int_ajust_aval')):
                     i.int_ajust_aval=lm.objects.filter(id_file=id,id_ligne=i.pk,field='int_ajust_aval').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='taille_l_min')):
                     i.taille_l_min=lm.objects.filter(id_file=id,id_ligne=i.pk,field='taille_l_min').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq2')):
                     i.uq2=lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq2').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='val_arrondie')):
                     i.val_arrondie=lm.objects.filter(id_file=id,id_ligne=i.pk,field='val_arrondie').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq3')):
                     i.uq3=lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq3').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='taille_lot_mx')):
                     i.taille_lot_mx=lm.objects.filter(id_file=id,id_ligne=i.pk,field='taille_lot_mx').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq4')):
                     i.uq4=lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq4').values_list()
        
   
        


        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='stock_maximum')):
                     i.stock_maximum=lm.objects.filter(id_file=id,id_ligne=i.pk,field='stock_maximum').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq5')):
                     i.uq5=lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq5').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='chant')):
                     i.chant=lm.objects.filter(id_file=id,id_ligne=i.pk,field='chant').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='typ')):
                     i.typ=lm.objects.filter(id_file=id,id_ligne=i.pk,field='typ').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='delai_sec')):
                     i.delai_sec=lm.objects.filter(id_file=id,id_ligne=i.pk,field='delai_sec').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='delai_sec1')):
                     i.delai_sec1=lm.objects.filter(id_file=id,id_ligne=i.pk,field='delai_sec1').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='ctrl_destinataire')):
                     i.ctrl_destinataire=lm.objects.filter(id_file=id,id_ligne=i.pk,field='ctrl_destinataire').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='article_rempl')):
                     i.article_rempl=lm.objects.filter(id_file=id,id_ligne=i.pk,field='article_rempl').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='dv')):
                     i.dv=lm.objects.filter(id_file=id,id_ligne=i.pk,field='dv').values_list()
        
   
        
       

        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='gml')):
                     i.gml=lm.objects.filter(id_file=id,id_ligne=i.pk,field='gml').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='grpl')):
                     i.grpl=lm.objects.filter(id_file=id,id_ligne=i.pk,field='grpl').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='abc')):
                     i.abc=lm.objects.filter(id_file=id,id_ligne=i.pk,field='abc').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq6')):
                     i.uq6=lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq6').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='element_dOTP')):
                     i.element_dOTP=lm.objects.filter(id_file=id,id_ligne=i.pk,field='element_dOTP').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='grpa')):
                     i.grpa=lm.objects.filter(id_file=id,id_ligne=i.pk,field='grpa').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='Code_pilotage')):
                     i.Code_pilotage=lm.objects.filter(id_file=id,id_ligne=i.pk,field='Code_pilotage').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='hierarch_produits')):
                     i.hierarch_produits=lm.objects.filter(id_file=id,id_ligne=i.pk,field='hierarch_produits').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='poids_brut')):
                     i.poids_brut=lm.objects.filter(id_file=id,id_ligne=i.pk,field='poids_brut').values_list()
        
        

        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='unp1')):
                     i.unp1=lm.objects.filter(id_file=id,id_ligne=i.pk,field='unp1').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='poids_net')):
                     i.poids_net=lm.objects.filter(id_file=id,id_ligne=i.pk,field='poids_net').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='unp2')):
                     i.unp2=lm.objects.filter(id_file=id,id_ligne=i.pk,field='unp2').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='pas_de_ccr')):
                     i.pas_de_ccr=lm.objects.filter(id_file=id,id_ligne=i.pk,field='pas_de_ccr').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='Taille_de_lot_du_CCR')):
                     i.Taille_de_lot_du_CCR=lm.objects.filter(id_file=id,id_ligne=i.pk,field='Taille_de_lot_du_CCR').values_list()
        elif(lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq7')):
                     i.uq7=lm.objects.filter(id_file=id,id_ligne=i.pk,field='uq7').values_list()
       
   
       
                
    r=rute.objects.all

    context['con']=condi
    context['data']=d
    context['id']=id
    context['rute']=r
   

    if request.method== 'POST':
      if(request.POST['choix']!="vide"):
        field=request.POST['choix']
        print("aaaaaattttttttttttttttttuuuuuuuuuuttttttttttttttttt")
        print(field)
        
        c=condition.objects.all().filter(id_rute=field)
        for i in c :
            x=i.field
            print(x ,"////////////filed condition")
            field_condition=str(x)
            condition_condition=i.Con
            print(condition_condition ,"////////////condition")
            # w=FileMs.objects.filter(**{y: e})
            # for y in w:
            c=resulta.objects.all().filter(id_condition=i)
            for m in c :
                    print(m.field ,"////////////filed resultat")
                    h=m.field
                    field_res=str(h)
                    condition_res=str(m.Res)
                    print(condition_res ,"//////////// resultat")
                    
                    w=FileMs.objects.filter(**{field_condition: condition_condition},file_id=id)
                    # .update(**{field_res:condition_res})
                    
                    for a in w :
                         
                         nu_case=nu_case+1
                         h=FileMs.objects.filter(pk=a.pk).get()
                         hh=FileMs.objects.filter(pk=a.pk).values_list(field_res,flat=True)
                         filee=File.objects.filter(id=a.file_id).get()
                         
                                

                         if(FileMs.objects.filter(**{field_condition: condition_condition} ,**{field_res: condition_res},pk=a.pk)):
                           case_non_treter=case_non_treter+1
                         else:
                                 ll= lm.objects.create(field=field_res,vieux=hh[0],nouveau=condition_res,id_condition=i,id_ligne=h,id_file=filee  )
                                 ll.save()
                                 N_case_modifier=N_case_modifier+1
                                 FileMs.objects.filter(pk=a.pk).update(**{field_res:condition_res})
                                 context['message']="modification avec sucssee"   
                         
                        
                        
                         print(h,"ttttttttttttttttttttttt",hh[0])

                    

                    # FileMs.objects.filter(blog=b).update(headline="Everything is the same")
        context['case']=nu_case
        context['m']=case_non_treter
        context['n']=N_case_modifier        
        context['class']="alert alert-success"
        context['cas']=0
 
      else:
        context['message']="choix n'est pas choisis" 
        context['class']="alert alert-danger"    
        context['cas']=1   
 
           
        
        return render(request,'import_file/import.html',context )






    
        
    return render(request,'import_file/import.html',context )
