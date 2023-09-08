
import io
from django.urls import reverse
from django.shortcuts import get_object_or_404, render,redirect
from .models import FileMs
from .models import condition,EquipeMS
from .models import File
import pandas as pd 
import psycopg2 
from django.contrib.auth.models import User
import xlwt
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import rute,resulta,lm,ChatMessage
from .forms import RuleForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import EquipeMS

# Create your views here.


def home(request):


  return render(request, 'home/index.html')


CustomUser = get_user_model()
def register(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        role = request.POST['role']
        if request.POST['role'] == "admin":
            is_staff = True
            is_superuser = True
        else:
            is_staff = False
            is_superuser = False
        CustomUser.objects.create_user(email=email, username=username, password=password, role=role, is_staff=is_staff, is_superuser=is_superuser)

        return redirect('log')
    return render(request, 'home/register.html')



def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
      
        user = CustomUser.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=username, password=password )
            if auth_user:
                login(request, auth_user)
                
                return render(request, 'home/profile.html')

            else:
                 return render(request, 'home/login.html', {'error_message': 'mot de pass incorrecte'})

        else:
            return render(request, 'home/login.html', {'error_message': 'User does not exist'})
           

    return render(request, 'home/login.html')


from django.contrib.auth import logout
from django.shortcuts import redirect 

def logout_view(request):
    logout(request)
    return redirect('home/index.html')



@login_required
def profile(request):

    return render(request,'home/profile.html')


# views.py


def is_manager(user):
 
    return user.USER_ROLE_CHOICES== 'manager'

#@user_passes_test(is_manager)

def is_admin(user):
 
    return user.USER_ROLE_CHOICES== 'admin'




def file(request):
    context = {}
    file=File.objects.all()
    context['data']=file

    return render(request,'import_file/file.html',context )

def upload(request):
    context = {}
   


    if request.method == "GET":

        
        return render(request , 'import_file/upload_file.html', context)
    
    
    if request.method== 'POST':
        
        file=request.FILES['my_file']
        



        
        
        conn=psycopg2.connect(host='localhost',dbname='1998_db',user='postgres',password='123456789',port='5432')
        import_ms_file(request,file,conn) 
        file=File.objects.all()
        context['data']=file       
       
    return render(request , 'import_file/file.html' , context)




def import_ms_file (request,file,conn):
    #read file pandas
    connn=psycopg2.connect(host='localhost',dbname='1998_db',user='postgres',password='123456789',port='5432')
    username = request.user
    ll= File.objects.create(name=file, imported_by=username.username)
    ll.save()
    dc=pd.read_excel(file)
    f=dc
    filee=pd.DataFrame(f)
    print( ll.id)
    print( ll.id) 
    print("///////////////////////////////" )
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
            table="home_filems",
            
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

###

def equipe_list(request):
    equipes = EquipeMS.objects.all()
    return render(request,'EquipeMS/list_ms.html', {'equipes': equipes})

def equipe_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        equipement = EquipeMS(name=name, email=email, Phone=Phone)
        equipement.save()
        return redirect('equipe_list')
    return render(request,'EquipeMS/list_ms.html')


def Edit(request):
    emp = EquipeMS.objects.all()
    context ={
        'emp':emp,
             }
    return redirect(request,'EquipeMS/list_ms.html',context)

def update(request,id):
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        equipement = EquipeMS(
            id=id,name=name, email=email, Phone=Phone)
        equipement.save()
        return redirect('equipe_list')
    return redirect(request,'EquipeMS/list_ms.html')

def delete(request, id):
    emp=EquipeMS.objects.filter(id=id)
    emp.delete()
    context ={
        'emp':emp,
             }
    
    return redirect('equipe_list')

def equipement_detail(request, id):
    equipement = get_object_or_404(EquipeMS, id=id)
    return render(request, 'EquipeMS/detail.html', {'equipement': equipement})






#@user_passes_test(is_manager)
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




from django.contrib.auth.decorators import login_required

@login_required
def rule_update(request, pk):
    rule = get_object_or_404(rute, pk=pk)
    
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
    context = {}
    if request.method == 'POST':
        delet_con.delete()
        cc=condition.objects.filter(id_rute=delet_con.id_rute)
        context['data']=cc
        return render(request,'condition/condition.html',context)
    return render(request, 'condition/condition.html', {' delet_con': delet_con})


def update_cond(request, condition_id):
    context = {}
    field=request.POST['field']
    con=request.POST['con']
    cond_obj = get_object_or_404(condition, pk=condition_id)
    cond_obj.field=field
    cond_obj.con=con
    cond_obj.save()
    
    cc=condition.objects.filter(id_rute=cond_obj.id_rute)
    context['data']=cc
    return render(request,'condition/condition.html',context)
    
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
    file=File.objects.all()
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
    
    return render(request,'import_file/import.html',context    )


def export (request,id):
      article=[]
      k=0
      if(request.POST['name']!="vide"):
        field=request.POST['name']  
        extension = '.xls'
        response = HttpResponse(content_type= 'application/ms-excel')
        response ['Content-Disposition'] ='attachment; filename={}/nouveau{}'.format(field, extension)
        
        wb = xlwt.Workbook (encoding='utf-8')
        
        ws = wb.add_sheet('Expenses')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = [
                
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
        for col_nun in range(len(columns)):
          ws.write(row_num, col_nun, columns[col_nun],font_style)

        font_style = xlwt.XFStyle()



        d=FileMs.objects.filter(file_id=id).values_list()
        for row in d :    
            row_num+=1
            x=0
            for col_num in range(len(row)-2):
                    x+=1
                    ws.write(row_num,col_num,str(row[x]),font_style)
                    

        wb.save(response)

                
       

      return response
  






from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage
from .ai_module import generate_response  # Importez la fonction depuis votre module d'IA

def chatbot(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        ChatMessage.objects.create(text="vou: " + user_input, is_user=True)
        bot_response = generate_response(user_input)  # Utilisez votre IA pour générer une réponse
        ChatMessage.objects.create(text="BOT: " + bot_response, is_user=False)

        return JsonResponse({'bot_response': bot_response})

    elif request.method == 'GET' and 'clear_history' in request.GET:
        ChatMessage.objects.all().delete()
        return redirect('chatbot')
    chat_history = ChatMessage.objects.all()
    return render(request, 'Chatbot/chat.html', {'chat_history': chat_history})






def test (request,id):
    context={}
    N_case_modifier=0
    nu_case=0
    case_non_treter=0
    
   
   
    condi=lm.objects.filter(id_file=id)
       
    r=rute.objects.all

    context['con']=condi
    context['data']=0
    context['id']=id
    context['rute']=r
   
    
   
    if(request.POST['test']!="vide"):
        field=request.POST['test']
        
        
        c=condition.objects.all().filter(id_rute=field)
        for i in c :
            x=i.field
            field_condition=str(x)
            condition_condition=i.Con
            c=resulta.objects.all().filter(id_condition=i)
            for m in c :
                    h=m.field
                    field_res=str(h)
                    condition_res=str(m.Res)
                    w=FileMs.objects.filter(**{field_condition: condition_condition},file_id=id)                    
                    for a in w :
                         nu_case=nu_case+1
                         h=FileMs.objects.filter(pk=a.pk).get()
                         hh=FileMs.objects.filter(pk=a.pk).values_list(field_res,flat=True)
                         filee=File.objects.filter(id=a.file_id).get()
                         if((FileMs.objects.filter(**{field_condition: condition_condition},**{field_res: condition_res},pk=a.pk).count())>0):
                           case_non_treter=case_non_treter+1
                         else:
                                 N_case_modifier=N_case_modifier+1  
                         

                     
        context['case']=nu_case
        if( nu_case == 0 ):
           context['faux']=0
           context['vrai']=100
        else:
             context['faux']=int((100*N_case_modifier)/nu_case)
             context['vrai']=int((100*case_non_treter)/nu_case)
                
        context['m']=case_non_treter
        context['n']=N_case_modifier
        context['class']="alert-warning alert-dismissible fade show"
        context['cas']=2
    else:
        context['message']="choix n'est pas choisis" 
        context['class']="alert alert-danger"
        context['cas']=1
       
    return render(request,'import_file/import.html',context )


from django.shortcuts import render
from .models import CustomUser

def count_users_by_role(request):
    user_count = CustomUser.objects.filter(role='user').count()
    manager_count = CustomUser.objects.filter(role='manager').count()
    admin_count = CustomUser.objects.filter(role='admin').count()
    
    return render(request, 'home/profile.html', {
        'user_count': user_count,
        'manager_count': manager_count,
        'admin_count': admin_count,
    })
