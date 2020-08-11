# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:55:24 2020

@author: aubaf
"""

class ficha(object):#no hereda de nadie
    def __init__(self,cod_vis,fecha,diag,prioridad,tipo,estado):#defino los atributos 
        self.set_cod_vis(cod_vis) #numero de visita secuencial
        self.set_fecha(fecha)
        self.set_diag(diag)
        self.set_prioridad(prioridad)
        self.set_tipo(tipo)
        self.set_estado(estado)
    #creo los sets de los diferentes atributos
    def set_cod_vis(self,cod_vis):
        self.__cod_vis=cod_vis
    def set_fecha(self,fecha):
        self.__fecha=fecha
    def set_diag(self,diag):
        self.__diag=diag
    def set_prioridad(self,prioridad):
        self.__prioridad=prioridad
    def set_tipo(self,tipo):
        self.__tipo=tipo
    def set_estado(self,estado):
        self.__estado=estado
    
    #creo los gets de los diferentes atributos
    def get_cod_vis(self):
        return self.__cod_vis
    def get_fecha(self):
        return self.__fecha
    def get_diag(self):
        return self.__diag
    def get_prioridad(self):
        return self.__prioridad
    def get_tipo(self):
        return self.__tipo
    def get_estado(self):
        return self.__estado
    
    def __str__(self):
        return "Código de visita: %s\n    Fecha: %s \n    Diagnóstico: %s \n    Prioridad: %s \n    Tipo de imagen: %s \n" %(self.__cod_vis, self.__fecha, self.__diag, self.__prioridad, self.__tipo)
    
    
    
    cod_vis=property(get_cod_vis,set_cod_vis)
    fecha=property(get_fecha,set_fecha)
    diag=property(get_diag,set_diag)
    prioridad=property(get_prioridad,set_prioridad)
    tipo=property(get_tipo,set_tipo)
    estado=property(get_estado,set_estado)