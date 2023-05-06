from django.urls import path 
from home import views
from .views import import_fil



urlpatterns = [
    path('', views.home,name='home'),
    path('import/', views.import_fil, name='import_fil'),
    path('delete_fil/', views.import_fil, name='delete_fil'),
      

   
]
 