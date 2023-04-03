from django.urls import path 
from home import views
from .views import import_excel


urlpatterns = [
    path('', views.home,name='home'),
    path('import/', views.import_excel, name='import_excel'),
    path('test', views.test,name='test'),
   
]
