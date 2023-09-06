from django.test import TestCase
from .models import EquipeMS
from .views import equipe_create
from django.urls import reverse
from django.test import RequestFactory


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

        
                                  
    def test_rule_create(self):
         w = self.rule_create()
         self.assertTrue(isinstance(w,rute))