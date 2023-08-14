from . import views

from django.urls import path 
from home import views




urlpatterns = [

    path('', views.home,name='home'),
    path('file/', views.file,name='file'),
    path('upload/', views.upload,name='upload'),
    path('delit<int:id>/', views.delit,name='delit'),
    
    path('filter<int:id>', views.filter,name='filter'),
    path('getfilter<int:id>', views.getfilter,name='getfilter'),
 
    
    path('rule_list/', views.rule_list, name='rule_list'), 
    path('rules/create/', views.rule_create, name='rule_create'),
    path('rules/<int:pk>/', views.rule_detail, name='rule_detail'),
    path('rules/<int:pk>/update/', views.rule_update, name='rule_update'),
    path('rules/<int:pk>/delete/', views.rule_delete, name='rule_delete'),
     
    path('condition/', views.Condition,name='Condition'),
    path('conditionall/', views.list_condition,name='List_condition'),
    
    path('condition/<int:id>/', views.conditionn,name='condition'),
    path('condution/<int:pk>/delete/', views.delete_condution, name='delete_condutionn'),
    
    path('resultat', views.resultas_all,name='resulta'),
    path('result_list', views.resultas_List,name='resultas_List'),
    path('resultat<int:id>', views.resulta_id,name='resultat'),
    
    
    
    path('table<int:id>', views.table,name='table'),
    



]
 