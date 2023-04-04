from django.shortcuts import render
import pandas as pd
import os
import psycopg2
from django.http import HttpResponse
from django.db import connection
from .models import mara_marc_for_MS
from django.http import HttpResponse



def home(request):
    return render(request,'home\index.html')
 

def import_fil(request):
    
    if request.method == 'POST':
    
      # establish connection
      conn = psycopg2.connect(
        host="localhost",
        database="ms_db",
        user="postgres",
        password="123456789"
      )
      # Read the Excel file into a DataFrame
      df = pd.read_excel('mara_marc_for_MS.xlsx', sheet_name='Sheet1', header=1)

      # Insert the DataFrame into the 'mara_marc_for_MS' table using the to_sql method
      df.to_sql(name='mara_marc_for_MS', con=conn, if_exists='append', index=False)

      # Close the database connection
      
      conn.close()

      # Traitez les données ici
    return render(request,'import_file/fil.html', {'message': 'Importation réussie!'})
  
    return render(request,'import_file/fil.html')



def test(request):
    return render(request,'home\index.html',{'name':'MSS'})