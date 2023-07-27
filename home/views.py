
import io
from django.urls import reverse
from django.shortcuts import get_object_or_404, render,redirect
from .models import FileMs
from .models import File
import pandas as pd 
import psycopg2 


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
    username = request.user.username
    user ="thouraya"
    print("thouuuuu")
    print(username)
    ll= File.objects.create(name=file,imported_by= user )
    ll.save()
    dc=pd.read_excel(file)
    f=dc
    filee=pd.DataFrame(f)

    filee.loc[:,'file_id']=ll.id
    msfilee=io.StringIO()
    msfilee.write(filee.to_csv(index=None,header=None))
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
                if( request.POST['choix'] == "Choose..." or request.POST['condition'] == ""):
                 
                 context['data']=d
               
                 context['list']=languages
                else:
                        choix=request.POST['choix']
                        con=request.POST['condition']
                        w=FileMs.objects.filter(**{choix: con},file_id=id)
                        context['list']=languages
                        context['data']=w
                        context['ms']='recherche dans la fileld '+choix +' le mot '+ con
                 
                
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











        









