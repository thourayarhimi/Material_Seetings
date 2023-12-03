from unittest.mock import Mock
from django.test import TestCase
from .models import EquipeMS
from .views import equipe_create
from django.urls import reverse
from django.test import RequestFactory

from django.test import TestCase , Client
from .models import EquipeMS
from .views import equipe_create
from django.urls import reverse
from django.test import RequestFactory
from .models import rute, condition, resulta , File, FileMs  # Make sure to import the models
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.

    
    
class EquipeCreateTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_equipe_create_post(self):
        # Créez une requête POST factice avec des données simulées
        data = {
            'name': 'thouraya',
            'email': 'thourayarhimi67@gmail.com',
            'Phone': '26873941'
        }
        request = self.factory.post(reverse('equipe_create'), data)

        # Appelez la fonction de vue pour créer l'équipe
        response = equipe_create(request)

        # Vérifiez si la réponse renvoie une redirection
        self.assertEqual(response.status_code, 302)  # 302 est le code HTTP pour une redirection

        # Vérifiez si l'équipe a été créée dans la base de données
        equipe = EquipeMS.objects.get(name='thouraya')
        self.assertEqual(equipe.name, 'thouraya')
        self.assertEqual(equipe.email, 'thourayarhimi67@gmail.com')
        self.assertEqual(equipe.Phone, 26873941)

    def test_equipe_create_get(self):
        # Créez une requête GET factice
        request = self.factory.get(reverse('equipe_create'))

        # Appelez la fonction de vue pour obtenir le formulaire
        response = equipe_create(request)

        # Vérifiez si la réponse renvoie un code de succès (200)
        self.assertEqual(response.status_code, 200)
###########
from .models import rute
class rule_createTest(TestCase):
    def rule_create(self,
  
                           name="thouraya",
                           created_by = "thouraya",
                           updated_by = "thouraya",

                    ):

    
        
     return  rute.objects.create(name=name, updated_by=updated_by, created_by=created_by)

########### Rule create ###########
class RuleCreateTest(TestCase):
    def rule_create(self, name="Rule_1"):
        return rute.objects.create(name=name)

    def test_rule_create(self):
        instance = self.rule_create()
        self.assertIsInstance(instance, rute)
        self.assertEqual(instance.name, "Rule_1")

########### Conditonn create ###########
class ConditionnTest(TestCase):
    def setUp(self):
        # Créez une règle (rute) pour les tests
        self.rule = rute.objects.create(name='Test Rule')

    def test_conditionn_add_condition(self):
        # Créez l'URL pour la vue conditionn avec l'ID de la règle
        url = reverse('condition', args=[self.rule.id])

        # Créez des données fictives pour la condition
        condition_data = {
            'choix': 'TestField',
            'condition': 'TestCondition',
        }

        # Envoyez une requête POST avec les données fictives
        response = self.client.post(url, condition_data)

        # Assurez-vous que la redirection s'est produite avec le statut HTTP 200
        self.assertEqual(response.status_code, 200)

        # Vérifiez si la condition a été correctement ajoutée à la règle
        conditions = condition.objects.filter(id_rute=self.rule)
        self.assertEqual(conditions.count(), 1)

        # Récupérez la condition nouvellement créée
        added_condition = conditions.first()

        # Assurez-vous que les champs de la condition correspondent aux données fictives
        self.assertEqual(added_condition.field, 'TestField')
        self.assertEqual(added_condition.Con, 'TestCondition')
        self.assertEqual(added_condition.id_rute, self.rule)

        # Assurez-vous que les données sont présentes dans le contexte de la réponse
        self.assertContains(response, 'TestField')
        self.assertContains(response, 'TestCondition')

########### Result create ###########
class ResultaIdTest(TestCase):
    
    def setUp(self):
       
        # Créez une instance de la classe rute pour être utilisée comme ForeignKey
        rute_instance = rute.objects.create(name='Rule_1')

        # Créez une condition pour les tests et associez-la à l'instance de rute créée
        self.condition = condition.objects.create(field='TestField', Con='TestCondition', id_rute=rute_instance)

    def test_resulta_id_create_resulta(self):
        # Créez l'URL pour la vue resulta_id avec l'ID de la condition
        url = reverse('resultat', args=[self.condition.id])

        # Créez des données fictives pour le résultat
        resulta_data = {
            'choix': 'TestField',
            'condition': 'TestCondition',
        } 

        # Envoyez une requête POST avec les données fictives
        response = self.client.post(url, resulta_data)
        print("Test For add Result  successfuly")
    
        # Assurez-vous que la redirection s'est produite avec le statut HTTP 200
        self.assertEqual(response.status_code, 200)

        # Vérifiez si le résultat a été correctement ajouté à la condition
        resultats = resulta.objects.filter(id_condition=self.condition)
        self.assertEqual(resultats.count(), 1)

        # Récupérez le résultat nouvellement créé
        added_resulta = resultats.first()

        # Assurez-vous que les champs du résultat correspondent aux données fictives
        self.assertEqual(added_resulta.field, 'TestField')
        self.assertEqual(added_resulta.Res, 'TestCondition')
        self.assertEqual(added_resulta.id_condition, self.condition)

        # Assurez-vous que les données sont présentes dans le contexte de la réponse
        self.assertContains(response, 'TestField')
        self.assertContains(response, 'TestCondition')

      

from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from unittest.mock import Mock
from home.models import File
from home.views import import_ms_file

class UploadTest(TestCase):
    def test_upload_view(self):
        # Create a test file content (CSV format)
        file_content = "article,designation_article,text_article,grpe_march,div,ctrpr,typ_app,a_s,tcy,dfi,dpr,horiz,mp,r,tyar,nal,i_c,aappr_def,mgapp,mag,tl,lot_fixe,uq1,stock_securite,uq0,tre,gest,di,rebut,gac,Profil,prpiAt,cree_par,langue,Cree_le,gcha,gs,mode_de_comparaison_des_besoin,int_ajust_amont,int_ajust_aval,taille_l_min,uq2,val_arrondie,uq3,taille_lot_mx,uq4,stock_maximum,uq5,chant,typ,delai_sec,delai_sec1,ctrl_destinataire,article_rempl,dv,gml,grpl,abc,uq6,element_dOTP,grpa,Code_pilotage,hierarch_produits,poids_brut,unp1,poids_net,unp2,pas_de_ccr,Taille_de_lot_du_CCR,uq7,file_id\n1,TestArticle,TestDescription,Group1,value1,value2,value3,value4,value5,value6,value7,value8,value9,value10,value11,value12,value13,value14,value15,value16,value17,value18,value19,value20,value21,value22,value23,value24,value25,value26,value27,value28,value29,value30,value31,value32,value33,value34,value35,value36,value37,value38,value39,value40,value41,value42,value43,value44,value45,value46,value47,value48,value49,value50,value51,value52,value53,value54,value55,value56,value57,value58,value59,value60,value61,value62,value63,value64,value65,value66,value67,value68,value69,value70,value71,value72,value73,value74,value75,value76,value77,value78,value79,value80,value81,value82,value83,value84,value85,value86,value87,value88,value89,value90,value91,value92,value93,value94,value95,value96,value97,value98,value99,value100,1"

        # Create a SimpleUploadedFile to simulate file upload
        test_file = SimpleUploadedFile("test_file.csv", file_content.encode())

        # Create a Django client to simulate the request
        client = Client()

        # Before the request
        print("Before request - File count:", File.objects.count())

        # Send a POST request to the view with the file
        response = client.post('/upload/', {'my_file': test_file})

        # Check the database after the request
        print("File count in the database:", File.objects.count())
        print("File objects in the database:", File.objects.all())

        # Ensure that the view returns a 200 status code upon success
        self.assertEqual(response.status_code, 200)
        

        # Ensure that the File model is saved in the database
        self.assertEqual(File.objects.count(), 1)
        saved_file = File.objects.first()
        self.assertEqual(saved_file.name, 'test_file.csv')
        self.assertEqual(saved_file.imported_by, '')  # Replace with the expected username

        # Ensure that the File model is saved in the database
        self.assertEqual(File.objects.count(), 1)
        saved_file_ms = File.objects.first()
        # Add more assertions based on your specific import logic and model fields

        # Clean up after the test if necessary
        saved_file.delete()
        saved_file_ms.delete()