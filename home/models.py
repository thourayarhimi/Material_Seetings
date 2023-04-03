from django.db import models

# Create your models here.

class Rule(models.Model):
    rule_name = models.CharField(max_length=200)
    comment = models.TextField(max_length=200)
    created_by = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Condition(models.Model):
    condition_number = models.IntegerField()
    field = models.FileField()
    value = models.TextField(max_length=200)
    created_by = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Result(models.Model):
    field = models.FileField()
    value = models.TextField(max_length=200)
    condition_number = models.IntegerField()
    created_by = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Profil(models.Model):
    name = models.CharField(max_length=200)
    comment = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
class Filed(models.Model):
    name = models.CharField(max_length=200)
    table = models.DateField()
    program =  models.CharField(max_length=200)
    tab =  models.CharField(max_length=200)
    
    
    
class mara_marc_for_MS(models.Model):
    article = models.TextField(max_length=200)
    designation_article =models.TextField(max_length=200)
    texte_article= models.TextField(max_length=200)
    grpe_march= models.TextField(max_length=200)
    div = models.IntegerField()
    ctrPr = models.TextField(max_length=200)
    typ_app= models.CharField(max_length=1)
    aS= models.IntegerField()
    tCy= models.IntegerField()
    dFI = models.IntegerField()
    dPr = models.IntegerField()
    horiz = models.IntegerField()
    mP = models.IntegerField()
    r = models.IntegerField()
    tyAr = models.TextField(max_length=200)
    nAl = models.IntegerField()
    iC  = models.IntegerField()
    aAppr_def  = models.IntegerField()
    mgApp = models.DateField()
    mag = models.DateField()
    tL = models.TextField(max_length=200)
    lot_fixe = models.IntegerField()
    uQ= models.CharField(max_length=1)
    stock_securite  = models.IntegerField()
    uQ_1= models.CharField(max_length=1)
    tRe = models.IntegerField()
    gest= models.TextField(max_length=200)
    di= models.TextField(max_length=200)
    rebut = models.FloatField()
    gAc = models.TextField(max_length=200)
    profil = models.TextField(max_length=200)
    prPiAt = models.TextField(max_length=200)
    cree_par= models.TextField(max_length=200)
    langue= models.TextField(max_length=200)
    cree_le_date  = models.DateField()
    gcha = models.IntegerField()
    gS  = models.IntegerField()
    mode_de_comparaison_des_besoin= models.IntegerField()
    int_ajust_amont = models.IntegerField()
    int_ajust_aval  = models.IntegerField()
    taille_l_min= models.BooleanField(default=False)
    uQ_2= models.TextField(max_length=200)
    val_arrondie  = models.BooleanField(default=False)
    uQ_3= models.TextField(max_length=200)
    taille_lot_mx = models.IntegerField()
    uQ_4= models.TextField(max_length=200)
    stock_maximum = models.IntegerField()
    uQ_5= models.TextField(max_length=200)
    chant= models.TextField(max_length=200)
    tyP= models.TextField(max_length=200)
    delai_sec = models.IntegerField()
    delai_sec_1 = models.IntegerField()
    ctrl_destinataire = models.CharField(max_length=100, null=True, blank=True)
    article_rempl= models.CharField(max_length=100, null=True, blank=True)
    dv= models.TextField(max_length=200)
    gML= models.TextField(max_length=200)
    grPl= models.TextField(max_length=200)
    aBC= models.CharField(max_length=1)
    uQ_6= models.TextField(max_length=200)
    elément_de_OTP = models.IntegerField()
    grpA   = models.IntegerField()
    code_pilotage  = models.IntegerField()
    hiérarch_produits  = models.IntegerField()
    poids_brut  = models.IntegerField()
    unP= models.TextField(max_length=200)
    poids_net = models.IntegerField()
    unP= models.TextField(max_length=200)
    pas_de_CCR = models.IntegerField()
    taille_de_lot_du_CCR = models.IntegerField()
    uQ_7= models.TextField(max_length=200)
    
    
    

    
    
  
 
   
 
     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

     
    
    
   
 
  