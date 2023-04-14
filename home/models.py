from django.db import models

# Create your models here.
#BasedModel

class BaseModel(models.Model) :

    created_at = models.DateTimeField(auto_now_add=True)  

    updated_at = models.DateTimeField(auto_now=True, null=True)

    created_by= models.CharField(max_length= 30, default='thouraya')

    updated_by = models.CharField(max_length= 30,default='thouraya')

   

    class Meta :

         #Django will not create a database table for this model

         abstract = True

 

#creating a custom model manager to apply the filter

#automatically without using filter(is_delete=False)

 

#SoftDeleteManager

class SoftDeleteManager(models.Manager):

    def get_queryset(self):

        return super().get_queryset().filter(is_deleted=False)
#SoftDeleteModel

class SoftDeleteModel(models.Model):

    is_deleted = models.BooleanField(null= False, default=False)

    deleted_by= models.CharField(max_length= 30,null=True)

    deleted_at = models.DateTimeField(auto_now_add=True,null=True)

    restored_at = models.DateTimeField(auto_now=True, null=True)

    restored_by = models.CharField(max_length= 30,default='Marwa',null=True)

   

    objects = models.Manager()

    undeleted_objects = SoftDeleteManager()

 

    def soft_delete(self):

        self.is_deleted = True

        self.save()

 

    def restore(self):

        self.is_deleted = False

        self.save()

   

 

    class Meta :

        #Django will not create a database table for this model

        abstract= True  
class Rule(BaseModel,SoftDeleteModel , models.Model):
    rule_name = models.CharField(max_length=200)
    comment = models.TextField(max_length=200)
 
    
    
class Condition(BaseModel,SoftDeleteModel, models.Model):
    condition_number = models.IntegerField()
    field = models.FileField()
    value = models.TextField(max_length=200)
  

class Result(BaseModel,SoftDeleteModel, models.Model):
    field = models.FileField()
    value = models.TextField(max_length=200)
    condition_number = models.IntegerField()
 
    
class Profil(BaseModel,SoftDeleteModel, models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField(max_length=200)
  
    
    
    
class Filed(BaseModel,SoftDeleteModel, models.Model):
    name = models.CharField(max_length=200)
    table = models.DateField()
    program =  models.CharField(max_length=200)
    tab =  models.CharField(max_length=200)
    tab_fr =  models.CharField(max_length=200)
     
    
    
    
class mara_marc_for_MS(BaseModel,SoftDeleteModel,models.Model):
    article = models.TextField(max_length=200)
    designation_article =models.TextField(max_length=200,blank=True,null=True)
    texte_article= models.TextField(max_length=200,blank=True,null=True)
    grpe_march= models.TextField(max_length=200,blank=True,null=True)
    div = models.IntegerField(blank=True,null=True)
    ctrPr = models.TextField(max_length=200,blank=True,null=True)
    typ_app= models.CharField(max_length=1,blank=True,null=True)
    aS= models.TextField(blank=True,null=True)
    tCy= models.IntegerField(blank=True,null=True)
    dFI = models.IntegerField(blank=True,null=True)
    dPr = models.IntegerField(blank=True,null=True)
    horiz = models.IntegerField(blank=True,null=True)
    mP = models.IntegerField(blank=True,null=True)
    r = models.TextField(blank=True,null=True)
    tyAr = models.TextField(max_length=200,blank=True,null=True)
    nAl = models.TextField(blank=True,null=True)
    iC  = models.TextField(blank=True,null=True)
    aAppr_def  = models.TextField(blank=True,null=True)
    mgApp = models.TextField(blank=True,null=True)
    mag = models.TextField(blank=True,null=True)
    tL = models.TextField(max_length=200,blank=True,null=True)
    lot_fixe = models.IntegerField(blank=True,null=True)
    uQ= models.CharField(max_length=1,blank=True,null=True)
    stock_securite  = models.IntegerField(blank=True,null=True)
    uQ_1= models.CharField(max_length=1,blank=True,null=True)
    tRe = models.IntegerField(blank=True,null=True)
    gest= models.TextField(max_length=200,blank=True,null=True)
    di= models.TextField(max_length=200,blank=True,null=True)
    rebut = models.FloatField(blank=True,null=True)
    gAc = models.TextField(max_length=200,blank=True,null=True)
    profil = models.TextField(max_length=200,blank=True,null=True)
    prPiAt = models.TextField(max_length=200,blank=True,null=True)
    cree_par= models.TextField(max_length=200,blank=True,null=True)
    langue= models.TextField(max_length=200,blank=True,null=True)
    cree_le_date  = models.DateField(blank=True,null=True)
    gcha = models.IntegerField(blank=True,null=True)
    gS  = models.TextField(blank=True,null=True)
    mode_de_comparaison_des_besoin= models.TextField(blank=True,null=True)
    int_ajust_amont = models.TextField(blank=True,null=True)
    int_ajust_aval  = models.TextField(blank=True,null=True)
    taille_l_min= models.BooleanField(default=False,blank=True,null=True)
    uQ_2= models.TextField(max_length=200,blank=True,null=True)
    val_arrondie  = models.BooleanField(default=False,blank=True,null=True)
    uQ_3= models.TextField(max_length=200,blank=True,null=True)
    taille_lot_mx = models.IntegerField(blank=True,null=True)
    uQ_4= models.TextField(max_length=200,blank=True,null=True)
    stock_maximum = models.IntegerField(blank=True,null=True)
    uQ_5= models.TextField(max_length=200,blank=True,null=True)
    chant= models.TextField(max_length=200,blank=True,null=True)
    tyP= models.TextField(max_length=200,blank=True,null=True)
    delai_sec = models.TextField(blank=True,null=True)
    delai_sec_1 = models.TextField(blank=True,null=True)
    ctrl_destinataire = models.CharField(max_length=100, null=True, blank=True)
    article_rempl= models.CharField(max_length=100, null=True, blank=True)
    dv= models.TextField(max_length=200,blank=True,null=True)
    gML= models.TextField(max_length=200,blank=True,null=True)
    grPl= models.TextField(max_length=200,blank=True,null=True)
    aBC= models.CharField(max_length=1,blank=True,null=True)
    uQ_6= models.TextField(max_length=200,blank=True,null=True)
    elément_de_OTP = models.TextField(blank=True,null=True)
    grpA   = models.TextField(blank=True,null=True)
    code_pilotage  = models.TextField(blank=True,null=True)
    hierarch_produits  = models.TextField(blank=True,null=True)
    poids_brut  = models.IntegerField(blank=True,null=True)
    unP= models.TextField(max_length=200,blank=True,null=True)
    poids_net = models.IntegerField(blank=True,null=True)
    unP_1= models.TextField(max_length=200,blank=True,null=True)
    pas_de_CCR = models.TextField(blank=True,null=True)
    taille_de_lot_du_CCR = models.IntegerField(blank=True,null=True)
    uQ_7= models.TextField(max_length=200,blank=True,null=True)
    
    
    

    
    
  
 
   
 
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

     
    
    
   
 
  