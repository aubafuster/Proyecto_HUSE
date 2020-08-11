# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 20:41:10 2020

@author: aubaf
"""


class paciente(object):
    
    def __init__(self,nombre,dni,id_num,sexo,edad,tel,email,grupo_sang,list_ficha): #defino los atributos

        self.set_nombre(nombre)
        self.set_dni(dni)
        self.set_id_num(id_num)
        self.set_sexo(sexo)
        self.set_edad(edad)
        self.set_tel(tel)
        self.set_email(email)
        self.set_grupo_sang(grupo_sang)
        self.set_list_ficha(list_ficha) #lista con las diferentes revisiones del paciente. Aqui guardo objetos tipo 
        #ficha cuyos atirbutos son todos los datos de la revision. Con estos datos el sistema calculará la prioridad del paciente para RM. 
    
    #creo los sets de los diferentes atributos     
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
    def set_dni(self,dni):
        self.__dni=dni
    def set_id_num(self,id_num):
        self.__id_num=id_num
    def set_sexo(self,sexo):
        self.__sexo=sexo
    def set_edad(self,edad):
        self.__edad=edad
    def set_tel(self,tel):
        self.__tel=tel
    def set_email(self,email):
        self.__email=email
    def set_grupo_sang(self,grupo_sang):
        self.__grupo_sang=grupo_sang
    def set_list_ficha(self,list_ficha):
        self.__list_ficha=list_ficha
    
    #creo los gets de los diferentes atributos    
    def get_nombre(self):
        return self.__nombre
    def get_dni(self):
        return self.__dni
    def get_id_num(self):
        return self.__id_num
    def get_sexo(self):
        return self.__sexo
    def get_edad(self):
        return self.__edad
    def get_tel(self):
        return self.__tel
    def get_email(self):
        return self.__email
    def get_grupo_sang(self):
        return self.__grupo_sang
    def get_list_ficha(self):
        return self.__list_ficha
    
    
    def __str__(self):
        fichas='\n    '
        for i in range(len(self.__list_ficha)):
            fichas+=str(self.__list_ficha[i])
            fichas+='\n    '
        return "NOMBRE: %s\nDNI: %s \nNÚMERO INDENT: %s \nSEXO: %s \nEDAD: %s \nTELÉFONO: %s \nEMAIL: %s \nGRUPO SANG: %s \nREVISION/ES: %s" %(self.__nombre, self.__dni, self.id_num, self.sexo, self.__edad, self.tel, self.email, self.grupo_sang, fichas)
    
    
    nombre=property(get_nombre,set_nombre)
    dni=property(get_dni,set_dni)
    id_num=property(get_id_num,set_id_num)
    sexo=property(get_sexo,set_sexo)
    edad=property(get_edad,set_edad)
    tel=property(get_tel,set_tel)
    email=property(get_email,set_email)
    grupo_sang=property(get_grupo_sang,set_grupo_sang)
    list_ficha=property(get_list_ficha,set_list_ficha)