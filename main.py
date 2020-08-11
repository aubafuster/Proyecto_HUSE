# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:21:30 2020

@author: aubaf
"""

from hospital import hospital
from interfaz_grafica import interfaz
from paciente import paciente
import pandas as pd

def main():
    dic_paciente={}
    id_num=1000
    
    datos=pd.read_csv('datos.csv',sep=';',encoding='latin-1') #para abrir cualquier archivo tiene que estar en formato CSV separado por comas
    
    for row in datos.itertuples():#recorro el archivo fila por fila
        p=paciente(row[1].title(),row[2],id_num,row[3],row[4],row[5],row[6],row[7],[])
        dic_paciente[id_num]=p
        id_num+=1
    
#    for i in range(len(dic_paciente)):
#        print(dic_paciente[i])
    
    h=hospital(dic_paciente)
    # Crear interface
    MainWindow =interfaz(h)
    MainWindow.crear_ventana_principal()
      
if __name__=="__main__":
    main()

