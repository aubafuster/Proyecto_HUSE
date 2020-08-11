# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:11:59 2020

@author: aubaf
"""

from datetime import datetime
from paciente import paciente
from ficha import ficha
import csv


class hospital(object): #hereda de datos
    def __init__(self,dic_paciente): #defino los atributos
        self.dic_paciente=dic_paciente

        
    def consult_pac(self,dni): #muestra la info de un paciente dado por teclado
        p='El paciente no existe'
        for i in self.dic_paciente:
            if dni == self.dic_paciente[i].dni:
                p=self.dic_paciente[i]
        return str(p)
    
    def consult_pac_nom(self,nom):
        lista=[] #lista vacia para introducir la info de los pacientes/medicos escogidos
        info=''
        for i in self.dic_paciente: #accedo al diccionario
            if nom == self.dic_paciente[i].nombre: #miro si el nombre introducido coincide con el nombre de algun objeto del diccionario
                lista.append(self.dic_paciente[i])#si es así lo añado a la lista (de esta manera soluciono el problema de nombres repetidos)
        for i in range (len(lista)):
            info+= str(lista[i])
            info+='\n\n'
        return info
    
    
    def comprueba_nomalta(self,dni,tipo): #metodo para comprobar que el nombre del paciente que se quiere dar de alta no existe ya en los diccionarios
        #este método sirve para cualquier objeto que se quiera dar de alta y depende del parámetro tipo. Esta distinción está por si se quisiera 
        #ampliar el sistema a otro tipo de objetos como médicos, enfermeros, etc. 
        bul=False
        if tipo=='P': #paciente
            for i in self.dic_paciente: #por cada elemento del diccionario de pacientes
                if dni == self.dic_paciente[i].dni: #si el nombre coincide con el de algún paciente
                    bul=True
            return bul
        
        
    def alta_paciente(self,nombre,dni,tel,email,grupo_sang,id_num,list_ficha,sexo,edad): #da de alta un paciente obteniendo la info por teclado (excepto id_num y list_ficha)
        p=paciente(nombre,dni,id_num,sexo,edad,tel,email,grupo_sang,list_ficha) #creo el objeto paciente
        self.dic_paciente[id_num]=p  #añado el objeto al diccionario usando como key el id_num
#
#    def onco1(self,dni,ing,tipo): #prioridad A/B
#        if ing=='Sí':
#            prioridad='Prioridad A'
#        else:
#            prioridad='Prioridad B'
#            
#        for i in self.dic_paciente:
#            if dni == self.dic_paciente[i].dni:
#                cod_vis=len(self.dic_paciente[i].list_ficha)
#        fecha=datetime.now()
#        diag='Seguimiento de paciente oncológico\n      con tratamiento activo y enfermedad inestable\n      o con sospecha de complicación'
#        f=ficha(cod_vis,fecha,diag,prioridad,tipo)
#        
#        for i in self.dic_paciente:
#            if dni == self.dic_paciente[i].dni:
#                self.dic_paciente[i].list_ficha.append(f)
#        
    def onco(self,dni,ing,tipo,ruta):
        if ruta == '1':
            if ing=='Sí':
                prioridad='Prioridad 1'
            else:
                prioridad='Prioridad 2'
            diag='Seguimiento de paciente oncológico con tratamiento activo y enfermedad inestable o con sospecha de complicación'
        
        if ruta == '2':
            prioridad='Prioridad 3'
            diag='Seguimiento de paciente oncológico con tratamiento activo y enfermedad estable'
        
        if ruta == '3':
            prioridad='Prioridad 4'
            diag='Seguimiento de paciente oncológico sin tratamiento activo y enfermedad estable'
        
        if ruta == 'NT':
            prioridad='Prioridad 2'
            diag='Primera prueba de imagen para sospecha de tumor en aparato musculoesqulético'
        
        if ruta == 'HPR':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en hueso plano. Lesión agresiva con sospecha de malignidad o dudas.'
        
        if ruta == 'HPT':
            prioridad = 'Prioridad 5'
            diag='Seguimiento de tumor en hueso plano. Lesión no agresiva y claramente benigna.'
        
        if ruta == 'tcHP':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en hueso plano.'
        
        if ruta == 'HLR':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en hueso largo con caracterización fundada y razonable. Lesión agresiva con sospecha de malignidad o dudas.'
        
        if ruta == 'HLT':
            prioridad = 'Prioridad 5'
            diag='Seguimiento de tumor en hueso largo con caracterización fundada y razonable. Lesión no agresiva y claramente benigna.'
        
        if ruta == 'tcHL':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en hueso largo. No caracterizable.'
        
        if ruta == 'ecoB':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en partes blandas.'
         
        if ruta == 'BR':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en partes blandas. Menor de 5cm, superficial a la fascia y con caracterización fundada y razonable. Lesión agresiva con sospecha de malignidad o dudas.'
        
        if ruta == 'BT':
            prioridad = 'Prioridad 5'
            diag='Seguimiento de tumor en partes blandas. Menor de 5cm, superficial a la fascia y con caracterización fundada y razonable. Lesión no agresiva y claramente benigna.'
        
        if ruta == 'tcBC':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en partes blandas. Mayor de 5cm, en profundidad a la fascia o no caracterizable. Matriz calcificante.'
        
        if ruta == 'tcBNC':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en partes blandas. Mayor de 5cm, en profundidad a la fascia o no caracterizable. Matriz NO calcificante.' 
       
        if ruta == 'BCR':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en partes blandas. Mayor de 5cm, en profundidad a la fascia o no caracterizable.Matriz calcificante. Lesión agresiva con sospecha de malignidad o dudas.'
       
        if ruta == 'BNCR':
            prioridad = 'Prioridad 2'
            diag='Seguimiento de tumor en partes blandas. Mayor de 5cm, en profundidad a la fascia o no caracterizable. Matriz NO calcificante. Lesión agresiva con sospecha de malignidad o dudas.'
        
        if ruta == 'BCT':
            prioridad = 'Prioridad 5'
            diag='Seguimiento de tumor en partes blandas. Mayor de 5cm, en profundidad a la fascia o no caracterizable. Matriz calcificante. Lesión no agresiva y claramente benigna.'
       
        if ruta == 'BNCT':
            prioridad = 'Prioridad 5'
            diag='Seguimiento de tumor en partes blandas. Mayor de 5cm, en profundidad a la fascia o no caracterizable.. Matriz NO calcificante. Lesión no agresiva y claramente benigna.'
        
        for i in self.dic_paciente:
            if dni == self.dic_paciente[i].dni:
                cod_vis=len(self.dic_paciente[i].list_ficha)+1
        fecha=datetime.now()
        estado=False
        f=ficha(cod_vis,fecha,diag,prioridad,tipo,estado)
        
        for i in self.dic_paciente:
            if dni == self.dic_paciente[i].dni:
                self.dic_paciente[i].list_ficha.append(f)
                
    def rodi(self,dni,tipo,ruta,extra):
        print(extra.get())
        if extra.get() == 'Sin sospechas':
            prioridad='Prioridad 3'
        if extra.get() == 'Sosp. enf reumatológica':
            prioridad='Prioridad 2'
        if extra.get() == 'Sospecha de infección':
            prioridad='Prioridad 1'
        
        if ruta == 'rxR':
            diag='Dolor agudo traumático de rodilla localizado. '+extra.get()
        if ruta == 'rxRPT':
            diag='Dolor agudo traumático de rodilla no localizado. No mejoría o nuevos síntomas en respuesta a tratamiento. '+extra.get()
        if ruta == 'RTN':
            diag='Dolor agudo traumático de rodilla no localizado pendiente de tratamiento. '+extra.get()
            prioridad='Prioridad 5'
        if ruta == 'RPTN':
            diag='Dolor agudo traumático de rodilla no localizado. Mejoría en respuesta a tratamiento. ' + extra.get()
            prioridad='Prioridad 5'
        if ruta == 'quiru':
            diag='Dolor postquirúrgico de rodilla'
        if ruta == 'lca':
            diag='Dolor de rodilla postquirúrgico. Lesión no protésica: LCA.'
        if ruta == 'osteo':
            diag='Dolor de rodilla postquirúrgico. Lesión no protésica: osteocondral.'
        if ruta=='meni':
            diag='Dolor de rodilla postquirúrgico. Lesión no protésica: meniscos.'
        if ruta=='p_tto':
            diag='Dolor de rodilla postquirúrgico. Lesión protésica: aflojamiento con causa aséptica.'
            prioridad='Prioridad 5'
        if ruta=='p_biop':
            diag='Dolor de rodilla postquirúrgico. Lesión protésica: aflojamiento con causa séptica.'
            prioridad='Prioridad 5'
        if ruta=='prote':
            diag='Dolor de rodilla postquirúrgico. Lesión protésica: aflojamiento.'
        if ruta =='rx_difuso':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso'
        if ruta =='rx_femo':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor femoro-patelar'
        if ruta=='norx_Difuso':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor  difuso. Sin indicaciones para realizar RX.'
            prioridad='Prioridad 5'
        if ruta=='norx_Femoro-patelar':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor femoro-patelar. Sin indicaciones para realizar RX.'
            prioridad='Prioridad 5'

            
        for i in self.dic_paciente:
            if dni == self.dic_paciente[i].dni:
                cod_vis=len(self.dic_paciente[i].list_ficha)+1
        fecha=datetime.now()
        estado=False
        f=ficha(cod_vis,fecha,diag,prioridad,tipo,estado)
        
        for i in self.dic_paciente:
            if dni == self.dic_paciente[i].dni:
                self.dic_paciente[i].list_ficha.append(f)
                
    def seg_rodi(self,dni,tipo,ruta,extra,subt,sos):            
        if extra.get() == 'Sin sospechas':
            prioridad='Prioridad 3'
        if extra.get() == 'Sosp. enf reumatológica':
            prioridad='Prioridad 2'
        if extra.get() == 'Sospecha de infección':
            prioridad='Prioridad 1'
            
        if ruta=='R1':
            prioridad='Prioridad 5'
            diag='Dolor agudo traumático de rodilla. Solución RX: Negativa. Pendiente de tratamiento.'
        if ruta == 'R2':
            prioridad='Prioridad 5'
            diag='Dolor agudo traumático de rodilla. Solución RX: '+subt.get()+' Pendiente de tratamiento.'
        if ruta=='R1PTN':
            prioridad='Prioridad 5'
            diag='Dolor agudo traumático de rodilla. Solución RX: Negativa. Mejoría en respuesta a tratamiento.'
        if ruta=='R2PTN':
            prioridad='Prioridad 5'
            diag='Dolor agudo traumático de rodilla. Solución RX: '+subt.get()+'. Mejoría en respuesta a tratamiento.'
        if ruta=='R1PT':
            diag='Dolor agudo traumático de rodilla. Solución RX: Negativa. No mejoría o nuevos síntomas en respuesta a tratamiento.'
        if ruta=='R2PT':
            diag='Dolor agudo traumático de rodilla. Solución RX: '+subt.get()+'. No mejoría o nuevos síntomas en respuesta a tratamiento.'
        if ruta=='R3':
            diag='Dolor agudo traumático de rodilla. Solución RX: daño interno adicional - '+ subt.get()
        if ruta == 'R4' or ruta =='R5':
            if sos.get()=='Sí':
                diag='Dolor agudo traumático de rodilla. Solución RX: '+ subt.get()+'. Sospecha de lesión vascular'
            if sos.get()=='No':
                diag='Dolor agudo traumático de rodilla. Solución RX: '+ subt.get()
        
        if ruta=='d_du_fin':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso: '+subt.get()+'. Tratado con éxito.'
            prioridad='Prioridad 5'
        if ruta=='d_seg_fin':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso tratado con éxito.'
            prioridad='Prioridad 5'
        if ruta=='f_seg_fin':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor femoro-patelar tratado con éxito.'
            prioridad='Prioridad 5'
        if ruta=='f_in_fin':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor femoro-patelar con inestabilidad tratado con éxito.'
            prioridad='Prioridad 5'
        if ruta=='eco_d_du':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso: '+subt.get()
        if ruta=='d_seg_tto':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso pendiente de tratamiento'
            prioridad='Prioridad 5'
        if ruta=='f_seg_tto':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor femoro-patelar pendiente de tratamiento'
            prioridad='Prioridad 5'
        if ruta=='f_in_tto':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor femoro-patelar con inestabilidad pendiente de tratamiento'
            prioridad='Prioridad 5'
        if ruta=='d_seg':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso persistente o con dudas.'
        if ruta=='d_du':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso: '+subt.get()+'. Persistente o con dudas.'
        if ruta=='f_seg':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor femoro-patelar persistente o con dudas.'
        if ruta=='f_in':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor femoro-patelar con inestabilidad. Sin mejoría o en estudio prequirúrgico.'
            
        if ruta=='mec':
            diag='Dolor de rodilla inestpecífico. Derrame, mecánico. '+subt.get()
        if ruta=='Nmec':
            diag='Dolor de rodilla inestpecífico. Derrame, NO mecánico. '+subt.get()
        if ruta=='ant':
            diag='Dolor de rodilla inespecífico. NO derrame, zona anterior: '+subt.get()
        if ruta=='med':
            diag='Dolor de rodilla inespecífico. NO derrame, zona medial: '+subt.get()
        if ruta=='lat':
            diag='Dolor de rodilla inespecífico. NO derrame, zona lateral: '+subt.get()
        if ruta=='pos':
            diag='Dolor de rodilla inespecífico. NO derrame, zona posterior: '+subt.get()
        if ruta=='l_mec':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso reumático. Derrame, mecánico. '+subt.get()
        if ruta=='l_Nmec':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso reumático. Derrame, NO mecánico. '+subt.get()
        if ruta=='l_ant':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso reumático. NO derrame, zona anterior: '+subt.get()
        if ruta=='l_med':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso reumático. NO derrame, zona medial: '+subt.get()
        if ruta=='l_lat':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso reumático. NO derrame, zona lateral: '+subt.get()
        if ruta=='l_pos':
            diag='Dolor de rodilla agudo/crónico NO traumático o por sobreuso. Dolor difuso reumático. NO derrame, zona posterior: '+subt.get()            
            
            
            
        for i in self.dic_paciente:
            if dni == self.dic_paciente[i].dni:
                cod_vis=len(self.dic_paciente[i].list_ficha)+1
        fecha=datetime.now()
        estado=False
        f=ficha(cod_vis,fecha,diag,prioridad,tipo,estado)
        
        for i in self.dic_paciente:
            if dni == self.dic_paciente[i].dni:
                self.dic_paciente[i].list_ficha.append(f)
    
    def gen_arch(self):
        lista=[]
        for i in self.dic_paciente:
            for j in range(len(self.dic_paciente[i].list_ficha)):
                if self.dic_paciente[i].list_ficha[j].estado==False:
                    rev={}
                    self.dic_paciente[i].list_ficha[j].estado=True
                    rev['Número de historial']=self.dic_paciente[i].dni
                    rev['Código de visita']=self.dic_paciente[i].list_ficha[j].cod_vis
                    rev['Fecha']=self.dic_paciente[i].list_ficha[j].fecha
                    rev['Diagnóstico']=self.dic_paciente[i].list_ficha[j].diag
                    rev['Prioridad']=self.dic_paciente[i].list_ficha[j].prioridad
                    rev['Tipo de imagen']=self.dic_paciente[i].list_ficha[j].tipo
                    lista.append(rev)
                    print(lista)
        keys=['Número de historial','Código de visita','Fecha','Diagnóstico','Prioridad','Tipo de imagen']
        f=open('neuvas_revisiones','w')
        dic=csv.DictWriter(f,keys)
        dic.writer.writerow(keys)
        dic.writerows(lista)
    
    def resumen_arch(self):
        lista=[]
        for i in self.dic_paciente:
            for j in range(len(self.dic_paciente[i].list_ficha)):
                rev={}
                rev['Número de historial']=self.dic_paciente[i].dni
                rev['Código de visita']=self.dic_paciente[i].list_ficha[j].cod_vis
                rev['Fecha']=self.dic_paciente[i].list_ficha[j].fecha
                rev['Diagnóstico']=self.dic_paciente[i].list_ficha[j].diag
                rev['Prioridad']=self.dic_paciente[i].list_ficha[j].prioridad
                rev['Tipo de imagen']=self.dic_paciente[i].list_ficha[j].tipo
                lista.append(rev)
        keys=['Número de historial','Código de visita','Fecha','Diagnóstico','Prioridad','Tipo de imagen']
        f=open('resumen_revisiones','w')
        dic=csv.DictWriter(f,keys)
        dic.writer.writerow(keys)
        dic.writerows(lista)
        
            
                
                
#    def onco2(self, dni, tipo): #prioridad C
#
#        prioridad='Prioridad C'
#
#        for i in self.dic_paciente:
#            if dni == self.dic_paciente[i].dni:
#                cod_vis=len(self.dic_paciente[i].list_ficha)
#        fecha=datetime.now()
#        diag='Seguimiento de paciente oncológico\n      con tratamiento activo y enfermedad estable'
#        f=ficha(cod_vis,fecha,diag,prioridad,tipo)
#        
#        for i in self.dic_paciente:
#            if dni == self.dic_paciente[i].dni:
#                self.dic_paciente[i].list_ficha.append(f)
#
#    def onco3(self, dni, tipo): #prioridad D
#        prioridad='Prioridad D'
#
#        for i in self.dic_paciente:
#            if dni == self.dic_paciente[i].dni:
#                cod_vis=len(self.dic_paciente[i].list_ficha)
#        fecha=datetime.now()
#        diag='Seguimiento de paciente oncológico\n      sin tratamiento activo y enfermedad estable'
#        f=ficha(cod_vis,fecha,diag,prioridad,tipo)
#        
#        for i in self.dic_paciente:
#            if dni == self.dic_paciente[i].dni:
#                self.dic_paciente[i].list_ficha.append(f)
    
#    def diag_onco(self, dni, tipo):
#        prioridad='Prioridad B'
#        
#        for i in self.dic_paciente:
#            if dni == self.dic_paciente[i].dni:
#                cod_vis=len(self.dic_paciente[i].list_ficha)
#        fecha=datetime.now()
#        diag='Primera prueba de imagen para sospecha de tumor en apartao musculoesqulético'
#        f=ficha(cod_vis,fecha,diag,prioridad,tipo)
#        
#        for i in self.dic_paciente:
#            if dni == self.dic_paciente[i].dni:
#                self.dic_paciente[i].list_ficha.append(f)

        
        
        
        
        
        
#    def alta_revision(self,p,fecha): #da de alta una revisión médica a un paciente
#        aleatorio=randint(0,len(self.dic_enfermero)-1) #creo un número aleatorio
#        enf=self.dic_enfermero[aleatorio] #escojo un enfermero al azar q llevará a cabo la alta
#        p=enf.asigna_revision(p,self.dic_medico,fecha)#le doy de alta la revision