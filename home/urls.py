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
 
    
    
    #path('rule_list/', views.rule_list, name='rule_list'), 
    #path('rules/create/', views.rule_create, name='rule_create'),
    #path('rules/<int:pk>/', views.rule_detail, name='rule_detail'),
    #path('rules/<int:pk>/update/', views.rule_update, name='rule_update'),
    #path('rules/<int:pk>/delete/', views.rule_delete, name='rule_delete'),
    
     

   
]
 