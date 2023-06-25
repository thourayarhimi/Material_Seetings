from . import views

from django.urls import path 
from home import views
from .views import import_fil
from .views import file_detail



urlpatterns = [
    path('', views.home,name='home'),
    path('import/', views.import_fil, name='import_fil'),
    path('delete_fil/', views.import_fil, name='delete_fil'),
    path('detail/', views.file_detail, name='file_detail'),
    
    
    path('rule_list/', views.rule_list, name='rule_list'), 
    path('rules/create/', views.rule_create, name='rule_create'),
    path('rules/<int:pk>/', views.rule_detail, name='rule_detail'),
    path('rules/<int:pk>/update/', views.rule_update, name='rule_update'),
    path('rules/<int:pk>/delete/', views.rule_delete, name='rule_delete'),
    
     

   
]
 