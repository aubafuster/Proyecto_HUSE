# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 21:07:07 2020

@author: aubaf
"""


import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image


class interfaz():

    def __init__(self, h):
        self.v = tk.Tk()
        self.v.geometry("900x780")
        self.v.title("GESTOR ASISTIDO DE DIAGNÓSTICO POR IMAGEN")
        self.h=h
        
    def crear_ventana_principal(self):
                
        #Imagen de fondo

        img = ImageTk.PhotoImage(Image.open("foto.gif"))
        panel = Label(self.v, image = img)
        panel.pack(side = "bottom", fill = "both", expand = "yes")

        #Barra de menu. 
        self.barraMenu=tk.Menu(self.v)
        
        # Diferents opcions
        self.mAlta = tk.Menu(self.barraMenu, tearoff=0)
        self.mRevision = tk.Menu(self.barraMenu, tearoff=0)
#        self.mCit = tk.Menu(self.barraMenu, tearoff=0)
#        self.mInf = tk.Menu(self.barraMenu, tearoff=0)
        self.mBuscar = tk.Menu(self.barraMenu, tearoff=0)
        self.mArchivos = tk.Menu(self.barraMenu, tearoff=0)
        self.mSalir = tk.Menu(self.barraMenu, tearoff=0)

        #Comandos
        
        #Menú de alta. 
        self.mAlta.add_command(label="Powerplan 1.0", command= self.no_desarrollado) 
        
        #Menú de revision.
        self.mRevision.add_command(label= "Alta paciente", command= self.alta_paciente) #Opcion para introducir al paciente en la base 
        #de datos. Sus datos generales seran requeridos.
        self.mRevision.add_command(label= "Primera visita", command= self.alta_revision)
        self.mRevision.add_command(label= "Seguimiento", command= self.rev_seguimiento)
        
#        self.mRevision.add_command(label= "Citación asistida", command= self.no_desarrollado) 
#        self.mRevision.add_command(label= "Informe estructurado asistido", command= self.no_desarrollado)
        
        #Menú de consultas
        self.mBuscar.add_command(label="Búsqueda por núm historial", command = self.consulta_paciente)
        self.mBuscar.add_command(label="Búsqueda por nombre", command = self.consulta_paciente_nom)
        
#        #Menú citacion
#        self.mCit.add_command(label="Citación", command= self.no_desarrollado)
#
#        #Menú informe
#        self.mInf.add_command(label="Informe", command= self.no_desarrollado)
        
        #Menú de archivos LO USARÉ PARA EXPORTAR LOS DATOS A UN CSV. 
        self.mArchivos.add_command(label= "Generar archivo", command= self.archivo)

        #Opción salir
        self.mSalir.add_command(label= "Salir", command= self.salir)

        #Agregar menus a la barra
        self.barraMenu.add_cascade(label = "Solicitud por catálogo", menu= self.mAlta)
        self.barraMenu.add_cascade(label = "Solicitud con decisión asistida (powerplan 2.0)", menu= self.mRevision)
#        self.barraMenu.add_cascade(label = "Citación asistida", menu= self.mCit)    
#        self.barraMenu.add_cascade(label = "Informe estructurado asisistido", menu= self.mInf)        
        self.barraMenu.add_cascade(label = "Buscador de pacientes", menu= self.mBuscar)
        self.barraMenu.add_cascade(label = "Exportar datos", menu= self.mArchivos)
        self.barraMenu.add_cascade(label = "Salir", menu= self.mSalir)
        
        #Indicar que la barra de menú está en la ventana
        self.v.config(menu = self.barraMenu)
        self.v.mainloop()
        
    """################################################################################
    ################################################################################
    ################################ SALIR Y NO DESARROLLADO #########################################
    ################################################################################ 
    ################################################################################"""     
    def salir(self):
        self.h.resumen_arch()
        self.v.destroy()
        
    def no_desarrollado(self):
        messagebox.showinfo(title='En desarrollo', message='Esta sección se desarrollará en futuras versiones.')
        
    """################################################################################
    ################################################################################
    ################################ ALTAS #########################################
    ################################################################################ 
    ################################################################################"""
      
                        
    def alta_paciente(self):
        """
        Funció que implementa una finestra per fer l'alta de pacient. 
        """
       
        #Preparo la nueva ventana para dar de alta al paciente
        v_ingresop = tk.Toplevel(self.v)
        v_ingresop.geometry("350x350")
        v_ingresop.title("Datos del paciente") 
        
        etiq_p= tk.Label(v_ingresop, text= "Insertar datos del paciente nuevo:")
        etiq_p.grid(column=0, row=0) #posicion
        
        # Nombre
        etiq_nom = tk.Label(v_ingresop, text= "Nombre y apellidos:") #label con informacion
        etiq_nom.grid(column=0, row=1) #posicion
        v_nom = tk.StringVar()
        v_nom.set("")
        e_nom = tk.Entry(v_ingresop, textvariable=v_nom) #aqui escribe el usuario
        e_nom.grid(column=1, row=1) #posicion
        
        # DNI
        etiq_dni = tk.Label(v_ingresop, text= "Núm. de historial clínico:")
        etiq_dni.grid(column=0, row=2)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_ingresop, textvariable=v_dni)
        e_dni.grid(column=1, row=2)
        

        # Telefono
        etiq_tlf = tk.Label(v_ingresop, text= "Teléfono:")
        etiq_tlf.grid(column=0, row=5)
        v_tlf = tk.StringVar()
        v_tlf.set("")
        e_tlf = tk.Entry(v_ingresop, textvariable=v_tlf)
        e_tlf.grid(column=1, row=5)
               
        # email
        etiq_email = tk.Label(v_ingresop, text= "Email:")
        etiq_email.grid(column=0, row=6)
        v_email = tk.StringVar()
        v_email.set("")
        e_email = tk.Entry(v_ingresop, textvariable=v_email)
        e_email.grid(column=1, row=6)
        
        # Grupo sanguineo (desplegable)
        etiq_sang = tk.Label(v_ingresop, text= "Grupo sanguíneo:")
        etiq_sang.grid(column=0, row=7)
        grup_sanguini = ['O+','A+','B+','O-','A-','AB+','B-','AB-']
        spin_sang = ttk.Combobox(v_ingresop, values=grup_sanguini, state="readonly")
        spin_sang.grid(column=1, row=7)
        
        # Sexo (desplegable)
        etiq_sexo = tk.Label(v_ingresop, text= "Sexo:")
        etiq_sexo.grid(column=0, row=8)
        sexos = ['Hombre','Mujer']
        spin_sexo = ttk.Combobox(v_ingresop, values=sexos, state="readonly")
        spin_sexo.grid(column=1, row=8)
        
        # edad
        etiq_edad = tk.Label(v_ingresop, text= "Edad:")
        etiq_edad.grid(column=0, row=9)
        v_edad = tk.StringVar()
        v_edad.set("")
        e_edad = tk.Entry(v_ingresop, textvariable=v_edad)
        e_edad.grid(column=1, row=9)
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.alta_pac_aux, v_nom, v_dni, v_tlf, v_email, spin_sang, spin_sexo, v_edad, v_ingresop)

        # Programar botó
        btnAsignar=tk.Button(v_ingresop,text="Dar alta", command = alta_pac_params).grid(column=1,row=11)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_ingresop,text="Salir", command = v_ingresop.destroy).grid(column=0,row=11) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_ingresop.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_ingresop.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_ingresop)
        
    def alta_pac_aux(self, nom, dni, tlf, email, sang, sexo, edad, v_ingresop):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([nom.get(), dni.get(), tlf.get(), email.get(), sang.get(), sexo.get(), edad.get() ]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == True: #si el paciente ya existe
            p=self.h.consult_pac(dni.get()) #guardo la info del paciente con el nombre introducido por teclado en una variable
            messagebox.showinfo(title='Paciente ya existente', message=p)
            #el paciente ya existe y tiene la informacion mostrada en el messagebox
            

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)
            id_num=len(self.h.dic_paciente) #id_num es la longitud del diccionario para seguir el orden
            list_ficha=[] #lista vacia
            #uso el metodo alta paciente de la clasee hospital para dar de alta
            self.h.alta_paciente(nom.get().title(), dni.get(), tlf.get(), email.get(), sang.get(), id_num, list_ficha, sexo.get(), edad.get())
            messagebox.showinfo(title='Añadido', message='Paciente añadido') #muestro confirmacion de que el paciente se ha añadido
            v_ingresop.destroy() #destruyo la ventana
    

    """################################################################################
    ################################################################################
    ################################ NUEVA REVISION #########################################
    ################################################################################ 
    ################################################################################"""
            
    def alta_revision(self):
         #Preparo la finestra
        v_new = tk.Toplevel(self.v) #creo la finestra
        v_new.geometry("275x210") #defineixo les seves dimensions
        v_new.title("Patología general") #li fico títol
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.new_rev_arti, v_new)
        alta_pac_params2=partial(self.new_rev_musc, v_new)
        alta_pac_params3=partial(self.new_rev_tum, v_new)
        
        # Programar botó

        etiq_p= tk.Label(v_new, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_new, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_new,text="Dolor articular", command = alta_pac_params).grid(column=2,row=2)
        
        etiq_p3= tk.Label(v_new, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        btnAsignar2=tk.Button(v_new,text="Patología muscular", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p4= tk.Label(v_new, text= "    ")
        etiq_p4.grid(column=2, row=8) #posicion
        btnAsignar3=tk.Button(v_new,text="Sospecha de tumor", command = alta_pac_params3).grid(column=2,row=10)
        
        etiq_p4= tk.Label(v_new, text= "    ")
        etiq_p4.grid(column=2, row=12) #posicion
        btnSortir=tk.Button(v_new,text="Salir", command = v_new.destroy).grid(column=2,row=14)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_new.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_new.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_new)
    
    def new_rev_arti(self, v_new):
        #Preparo la finestra
        v_tipo = tk.Toplevel(self.v) #creo la finestra
        v_tipo.geometry("275x210") #defineixo les seves dimensions
        v_tipo.title("Dolor articular") #li fico títol
        
        etiq_p= tk.Label(v_tipo, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        
        # Tipo (desplegable)
        etiq_t = tk.Label(v_tipo, text= "Tipo:")
        etiq_t.grid(column=1, row=2)
        tipos = ['Sin sospechas','Sosp. enf reumatológica','Sospecha de infección']
        spin_t = ttk.Combobox(v_tipo, values=tipos, state="readonly")
        spin_t.grid(column=2, row=2)
        
        etiq_p= tk.Label(v_tipo, text= "    ")
        etiq_p.grid(column=1, row=3) #posicion
        
        # Zona (desplegable)
        etiq_z = tk.Label(v_tipo, text= "Zona:")
        etiq_z.grid(column=1, row=4)
        zonas = ['Rodilla']
#        zonas = ['Hombro','Codo','Mano y muñeca','Cadera','Articulaciones sacroilíacas','Rodilla','Tobillo y pie','Columna cervical','Columna dorsal y lumbar','Estenosis de canal','Escoliosis']
        spin_z = ttk.Combobox(v_tipo, values=zonas, state="readonly")
        spin_z.grid(column=2, row=4)
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.new_rev_zonas, spin_t, spin_z, v_tipo, v_new)
        
        etiq_p= tk.Label(v_tipo, text= "    ")
        etiq_p.grid(column=1, row=6) #posicion
        btnAsignar3=tk.Button(v_tipo,text="Continuar", command = alta_pac_params).grid(column=2,row=8)
        
        btnSortir=tk.Button(v_tipo,text="Atrás", command = v_tipo.destroy).grid(column=1,row=8)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_tipo.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_tipo.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_tipo)
        
        
    def new_rev_musc(self,v_new):
        messagebox.showinfo(title='En desarrollo', message='Esta sección se desarrollará en futuras versiones.')
#        #Preparo la finestra
#        v_tipo = tk.Toplevel(self.v) #creo la finestra
#        v_tipo.geometry("275x210") #defineixo les seves dimensions
#        v_tipo.title("Patología muscular") #li fico títol
#        
#        etiq_p= tk.Label(v_tipo, text= "    ")
#        etiq_p.grid(column=0, row=0) #posicion
#        
#        # Tipo (desplegable)
#        etiq_t = tk.Label(v_tipo, text= "Tipo:")
#        etiq_t.grid(column=1, row=2)
#        tipos = ['Sin signos alarma','Con signos alarma']
#        spin_t = ttk.Combobox(v_tipo, values=tipos, state="readonly")
#        spin_t.grid(column=2, row=2)
#        
#        etiq_p= tk.Label(v_tipo, text= "    ")
#        etiq_p.grid(column=1, row=3) #posicion
#        
#        
#        # de la llibreria functools
#        # assignar parcial per a funció, per a poder assignar directament command amb variables
#        #accedim al métode auxiliar
#        alta_pac_params=partial(self.new_rev_musc_result, spin_t, v_tipo, v_new)
#        
#        etiq_p= tk.Label(v_tipo, text= "    ")
#        etiq_p.grid(column=1, row=6) #posicion
#        btnAsignar3=tk.Button(v_tipo,text="Continuar", command = alta_pac_params).grid(column=2,row=8)
#        
#        btnSortir=tk.Button(v_tipo,text="Salir", command = v_tipo.destroy).grid(column=1,row=8)
#
#        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
#        v_tipo.transient()
#
#        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
#        v_tipo.grab_set()
#
#        # Wait for the window to end
#        self.v.wait_window(v_tipo)
        
    def new_rev_tum(self,v_new):
#        #Preparo la finestra
#        v_tipo = tk.Toplevel(self.v) #creo la finestra
#        v_tipo.geometry("275x210") #defineixo les seves dimensions
#        v_tipo.title("Sospecha de tumor") #li fico títol
#        
#        etiq_p= tk.Label(v_tipo, text= "    ")
#        etiq_p.grid(column=0, row=0) #posicion
#        
#        # Tipo (desplegable)
#        etiq_t = tk.Label(v_tipo, text= "Tipo:")
#        etiq_t.grid(column=1, row=2)
#        tipos = ['Partes blandas','Óseo']
#        spin_t = ttk.Combobox(v_tipo, values=tipos, state="readonly")
#        spin_t.grid(column=2, row=2)
#        
#        etiq_p= tk.Label(v_tipo, text= "    ")
#        etiq_p.grid(column=1, row=3) #posicion
#        
#        # Zona (desplegable)
#        etiq_z = tk.Label(v_tipo, text= "Zona:")
#        etiq_z.grid(column=1, row=4)
#        zonas = ['Hombro','Codo','Mano y muñeca','Cadera','Articulaciones sacroilíacas','Rodilla','Tobillo y pie','Columna cervical','Columna dorsal y lumbar','Estenosis de canal','Escoliosis']
#        spin_z = ttk.Combobox(v_tipo, values=zonas, state="readonly")
#        spin_z.grid(column=2, row=4)
#        
#        # de la llibreria functools
#        # assignar parcial per a funció, per a poder assignar directament command amb variables
#        #accedim al métode auxiliar
#        alta_pac_params=partial(self.new_rev_zonas3, spin_t, spin_z, v_tipo)
#        
#        etiq_p= tk.Label(v_tipo, text= "    ")
#        etiq_p.grid(column=1, row=6) #posicion
#        btnAsignar3=tk.Button(v_tipo,text="Continuar", command = alta_pac_params).grid(column=2,row=8)
#        
#        btnSortir=tk.Button(v_tipo,text="Salir", command = v_tipo.destroy).grid(column=1,row=8)
#
#        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
#        v_tipo.transient()
#
#        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
#        v_tipo.grab_set()
#
#        # Wait for the window to end
#        self.v.wait_window(v_tipo)
        messagebox.showinfo(title='Procedimiento', message='Primera prueba a realizar: RX 2 proyecciones.\n\nUna vez realizada acceder a apartado Revisión > Seguimiento > Oncológico > Proceso de diagnóstico')    
        
        #Preparo la nueva ventana para dar de alta al paciente
        v_so = tk.Toplevel(self.v)
        v_so.geometry("550x350")
        v_so.title("Resumen y guardar") 
        
        etiq_p= tk.Label(v_so, text= "Resumen del diagnóstico:\n    Sospecha de tumor en aparato musculo-esquelético.")
        etiq_p.grid(column=0, row=0) #posicion
        

        
        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_so, text= "Tipo de prueba de imagen")
        etiq_t.grid(column=0, row=4)
        op = ['RX 2 proyecciones']
        spin_t = ttk.Combobox(v_so, values=op, state="readonly")
        spin_t.grid(column=1, row=4)
        
        # DNI
        etiq_dni = tk.Label(v_so, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_so, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_so, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_so, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.new_rev_tum_aux, v_dni, spin_t, v_so, v_new)

        # Programar botó
        btnAsignar=tk.Button(v_so,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
        
    def new_rev_tum_aux(self, dni, tipo, v_so, v_new):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([dni.get(),tipo.get()]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
            messagebox.showinfo(title='Paciente no existente', message='El paciente con este número de historial clínico no existe')

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)
            ruta='NT'
            ing=None
            self.h.onco(dni.get(),ing,tipo.get(),ruta)
            
            messagebox.showinfo(title='Guardado', message='Diagnóstico guardado') #muestro confirmacion de que el paciente se ha añadido
            messagebox.showinfo(title='En desarrollo', message='Las siguientes secciones de Citación e Informes se desarrollarán en futuras versiones.')    
            v_so.destroy() #destruyo la ventana
            v_new.destroy()
            
            
    def new_rev_zonas(self, extra, zona, v_tipo, v_new):
        if zona.get() == 'Rodilla':
             #Preparo la finestra
            v_rod = tk.Toplevel(self.v) #creo la finestra
            v_rod.geometry("600x400") #defineixo les seves dimensions
            v_rod.title("Escenarios clínicos") #li fico títol
            
            
            # de la llibreria functools
            # assignar parcial per a funció, per a poder assignar directament command amb variables
            #accedim al métode auxiliar
            alta_pac_params=partial(self.rod_trauma, extra, v_rod, v_tipo, v_new)
            alta_pac_params2=partial(self.rod_uso, extra, v_rod, v_tipo, v_new)
            alta_pac_params3=partial(self.rod_quiru, extra, v_rod, v_tipo, v_new)
            alta_pac_params4=partial(self.rod_ines, extra, v_rod, v_tipo, v_new)
            alta_pac_params5=partial(self.bultoma, v_rod, v_tipo, v_new)            
            
            # Programar botó
            
            etiq_p= tk.Label(v_rod, text= "    ")
            etiq_p.grid(column=0, row=0) #posicion
            etiq_p2= tk.Label(v_rod, text= "    ")
            etiq_p2.grid(column=2, row=0) #posicion
            btnAsignar=tk.Button(v_rod,text="Dolor agudo traumático", command = alta_pac_params).grid(column=2,row=2)
            
    
            etiq_p3= tk.Label(v_rod, text= "    ")
            etiq_p3.grid(column=2, row=4) #posicion
            
            btnAsignar2=tk.Button(v_rod,text="Dolor agudo/crónico NO traumático o por sobreuso", command = alta_pac_params2).grid(column=2,row=6)
            
            etiq_p4= tk.Label(v_rod, text= "    ")
            etiq_p4.grid(column=2, row=8) #posicion
            
            btnAsignar3=tk.Button(v_rod,text="Dolor postquirúrgico", command = alta_pac_params3).grid(column=2,row=10)
            
            etiq_p5= tk.Label(v_rod, text= "    ")
            etiq_p5.grid(column=2, row=12) #posicion
            
            btnAsignar4=tk.Button(v_rod,text="Dolor inespecífico", command = alta_pac_params4).grid(column=2,row=14)

            etiq_p5= tk.Label(v_rod, text= "    ")
            etiq_p5.grid(column=2, row=16) #posicion
            
            btnAsignar5=tk.Button(v_rod,text="Bultoma", command = alta_pac_params5).grid(column=2,row=18)
            
            etiq_p6= tk.Label(v_rod, text= "    ")
            etiq_p6.grid(column=2, row=20) #posicion
            
            btnSortir=tk.Button(v_rod,text="Atrás", command = v_rod.destroy).grid(column=2,row=22)
    
            # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
            v_rod.transient()
    
            #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
            v_rod.grab_set()
    
            # Wait for the window to end
            self.v.wait_window(v_rod)
            
    def bultoma(self, v_rod, v_tipo, v_new):
        v_rod.destroy()
        v_tipo.destroy()  
        self.new_rev_tum(v_new)    
        
    def rod_trauma(self, extra, v_rod, v_tipo, v_new):
        #Preparo la finestra
        v_i = tk.Toplevel(self.v) #creo la finestra
        v_i.geometry("490x200") #defineixo les seves dimensions
        v_i.title("Localización del dolor") #li fico títol
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        ruta='R'
        v_m=None
        v_so=None
        alta_pac_params=partial(self.sol_rx_rod, ruta, extra, v_m, v_so, v_i, v_rod, v_tipo,v_new)
        alta_pac_params2=partial(self.tto_rod, extra, v_i, v_rod, v_tipo,v_new)
        
        # Programar botó
        
        etiq_p= tk.Label(v_i, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_i, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_i,text="Dolor localizado: Derrame, NO deambulación, NO flexión 90º.", command = alta_pac_params).grid(column=2,row=2)
        
        etiq_p3= tk.Label(v_i, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_i,text="Dolor NO localizado: NO derrame, deambulación, flexión 90º.", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p4= tk.Label(v_i, text= "    ")
        etiq_p4.grid(column=2, row=8) #posicion
        
        btnSortir=tk.Button(v_i,text="Atrás", command = v_i.destroy).grid(column=2,row=10)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_i.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_i.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_i)
    
    def tto_rod(self, extra, v_i, v_rod, v_tipo, v_new):
        ruta='RT'
        v_so = tk.Toplevel(self.v)
        v_so.geometry("400x250")
        v_so.title("TTO") 
        
        etiq_p= tk.Label(v_so, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_so, text= "¿Se le ha aplicado tratamiento al paciente?")
        etiq_p.grid(column=2, row=2) #posicion
        
        v_m=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_new_rod,ruta, extra, v_m, v_so, v_i, v_rod, v_tipo, v_new)
        alta_pac_params2=partial(self.mej_rod,ruta, extra, v_so, v_i, v_rod, v_tipo, v_new)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_so,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_so,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
    
    def mej_rod(self, ruta, extra, v_so, v_i, v_rod, v_tipo, v_new):
        ruta='RPT'
        v_m = tk.Toplevel(self.v)
        v_m.geometry("350x250")
        v_m.title("TTO") 
        
        etiq_p= tk.Label(v_m, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_m, text= "Respuesta al tratamiento")
        etiq_p.grid(column=2, row=2) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_new_rod, ruta, extra, v_m, v_so, v_i, v_rod, v_tipo, v_new)
        alta_pac_params2=partial(self.sol_rx_rod, ruta, extra, v_m, v_so, v_i, v_rod, v_tipo, v_new)
        
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_m,text="Mejoría", command = alta_pac_params).grid(column=2,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        btnAsignar2=tk.Button(v_m,text="No mejoría o nuevos signos de alarma", command = alta_pac_params2).grid(column=2,row=10)
        
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=12) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_m,text="Atrás", command = v_m.destroy).grid(column=2,row=14) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_m.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_m.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_m)
    
    def sol_new_rod(self,ruta, extra, v_m, v_so, v_i, v_rod, v_tipo, v_new):

        #Preparo la nueva ventana para dar de alta al paciente
        v_sol = tk.Toplevel(self.v)
        v_sol.geometry("650x350")
        v_sol.title("Resumen y guardar") 
        
        if ruta=='RPT':
            etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla no localizado. Mejoría en respuesta a tratamiento.")
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Fin del estudio.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            ruta='RPTN'
        if ruta=='RT':
            etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla no localizado pendiente de tratamiento.")
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Aplicar tratamiento.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            ruta='RTN'
        
        # DNI
        etiq_dni = tk.Label(v_sol, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_sol, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_new_rod_aux, v_dni, spin_t, ruta, extra, v_sol, v_m, v_so, v_i, v_rod, v_tipo, v_new)

        # Programar botó
        btnAsignar=tk.Button(v_sol,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_sol,text="Atrás", command = v_sol.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_sol.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_sol.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_sol)
        
    def sol_rx_rod(self, ruta, extra, v_m, v_so, v_i, v_rod, v_tipo,v_new):
        
        #Preparo la nueva ventana para dar de alta al paciente
        v_sol = tk.Toplevel(self.v)
        v_sol.geometry("650x350")
        v_sol.title("Resumen y guardar") 
        
        if ruta=='RPT':
            etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla no localizado.\nNo mejoría o nuevos síntomas en respuesta a tratamiento.")
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RX AP y Lateral en descarga']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            ruta='rxRPT'
        if ruta=='R':
            etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla localizado.")
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RX AP y Lateral en descarga']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            ruta='rxR'
        
        # DNI
        etiq_dni = tk.Label(v_sol, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_sol, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_new_rod_aux, v_dni, spin_t, ruta, extra, v_sol, v_m, v_so, v_i, v_rod, v_tipo, v_new)

        # Programar botó
        btnAsignar=tk.Button(v_sol,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_sol,text="Atrás", command = v_sol.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_sol.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_sol.grab_set()
        
    def sol_new_rod_aux(self, dni, tipo, ruta, extra, v_sol, v_m, v_so, v_i, v_rod, v_tipo, v_new):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([dni.get(),tipo.get()]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
            messagebox.showinfo(title='Paciente no existente', message='El paciente con este núemro de historial clínico no existe')

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)
            self.h.rodi(dni.get(),tipo.get(),ruta,extra)
            messagebox.showinfo(title='Guardado', message='Diagnóstico guardado') #muestro confirmacion de que el paciente se ha añadido
            messagebox.showinfo(title='En desarrollo', message='Las siguientes secciones de Citación e Informes se desarrollarán en futuras versiones.')                


            v_sol.destroy()
            v_new.destroy()
            v_tipo.destroy()
            v_rod.destroy()
            if ruta!='quiru':
                v_i.destroy()
            if ruta!='rxR' and ruta!='quiru' and ruta!='rx_difuso' and ruta!='rx_femo' and ruta!='norx_Difuso' and ruta!='norx_Femoro-patelar':
                v_so.destroy()
            if ruta!='rxR' and ruta!='RTN' and ruta!='quiru' and ruta!='rx_difuso' and ruta!='rx_femo' and ruta!='norx_Difuso' and ruta!='norx_Femoro-patelar':
                v_m.destroy()
    
    def rod_uso(self, extra, v_rod, v_tipo, v_new):
        v_t = tk.Toplevel(self.v)
        v_t.geometry("850x550")
        v_t.title("Seleccionar") 
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion

        texto = tk.Label(v_t, text= "INFO IMPORTANTE: Si ya ha realizado RX acceder a apartado\nSolicitud > Seguimiento > Dolor articular > Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\n\n\n Indicaciones:\n    1. Traumatismo no estudiado con signos de reglas de Ottawa\n    2. Historial complejo\n    3. Derrame significativo sin radiografías\n    4. Pérdida de movilidad sin causa clara\n    5. Inicio agudo / subagudo\n    6. Bloqueo intermitente\n    7. Sin alivio tras 4 semanas de tratamiento conservador\n    8. Masa de aumento palpable\n    9. Prótesis dolorosa\n\n")
        texto.grid(column=2, row=2)
        
        etiq_t = tk.Label(v_t, text= "¿Se cumple alguna de las indicaciones previas?")
        etiq_t.grid(column=2, row=4)
        op = ['Sí','No']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=4, row=4)

        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=6) #posicion
                
        etiq_s = tk.Label(v_t, text= "Tipo de dolor")
        etiq_s.grid(column=2, row=8)
        op = ['Difuso','Femoro-patelar']
        spin_s = ttk.Combobox(v_t, values=op, state="readonly")
        spin_s.grid(column=4, row=8)
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=10) #posicion

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rx_uso, extra, spin_t, spin_s, v_t, v_rod, v_tipo, v_new)
        

        # Programar botó
        btnAsignar=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=12)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=12) #boton salir: se cierra la ventana
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=14) #posicion


        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)
    
    def sol_rx_uso(self, extra, prueba , ti_dolor, v_t, v_rod, v_tipo, v_new):    
        #Preparo la nueva ventana para dar de alta al paciente
        v_sol = tk.Toplevel(self.v)
        v_sol.geometry("560x450")
        v_sol.title("Resumen y guardar") 

        if prueba.get() =='Sí':
            if ti_dolor.get()=='Difuso':
                etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso")
                etiq_p.grid(column=0, row=0) #posicion
                # Tipo de prueba de imagen (desplegable)
                etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
                etiq_t.grid(column=0, row=4)
                op = ['RX AP y Lateral en carga']
                spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
                spin_t.grid(column=1, row=4)
                ruta='rx_difuso'
            if ti_dolor.get() =='Femoro-patelar':
                etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor femoro-patelar")
                etiq_p.grid(column=0, row=0) #posicion
                # Tipo de prueba de imagen (desplegable)
                etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
                etiq_t.grid(column=0, row=4)
                op = ['RX AP, Lateral y axial en carga']
                spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
                spin_t.grid(column=1, row=4)
                ruta='rx_femo'
        if prueba.get()=='No':
            etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor " + ti_dolor.get() + '. Sin indicaciones para realizar RX.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas indicadas. Pendiente de tratamiento conservador.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            ruta='norx_'+ti_dolor.get()

        # DNI
        etiq_dni = tk.Label(v_sol, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_sol, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        v_m=None
        v_so=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_new_rod_aux, v_dni, spin_t, ruta, extra, v_sol, v_m, v_so, v_t, v_rod, v_tipo, v_new)

        # Programar botó
        btnAsignar=tk.Button(v_sol,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_sol,text="Atrás", command = v_sol.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_sol.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_sol.grab_set()        
        
    def rod_quiru(self, extra, v_rod, v_tipo, v_new):
        messagebox.showinfo(title='Procedimiento', message='Primera prueba a realizar: RX AP y Lateral en carga.\n\nUna vez realizada acceder a apartado Revisión > Seguimiento > Dolor articular > Dolor postquirúrgico')    
        ruta='quiru'
        #Preparo la nueva ventana para dar de alta al paciente
        v_sol = tk.Toplevel(self.v)
        v_sol.geometry("450x350")
        v_sol.title("Resumen y guardar") 

        etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor postquirúrgico de rodilla.")
        etiq_p.grid(column=0, row=0) #posicion
        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
        etiq_t.grid(column=0, row=4)
        op = ['RX AP y Lateral en carga']
        spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
        spin_t.grid(column=1, row=4)

        # DNI
        etiq_dni = tk.Label(v_sol, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_sol, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        v_m=None
        v_so=None
        v_i=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_new_rod_aux, v_dni, spin_t, ruta, extra, v_sol, v_m, v_so, v_i, v_rod, v_tipo, v_new)

        # Programar botó
        btnAsignar=tk.Button(v_sol,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_sol,text="Atrás", command = v_sol.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_sol.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_sol.grab_set()
        
    def rod_ines(self, extra, v_rod, v_tipo, v_new):
        ruta=None
        v_r=None
        v_p=None
        self.seg_rod_ines(ruta,extra,v_r,v_p,v_rod,v_tipo,v_new)
#    def new_rev_musc_result(self, extra, v_tipo, v_new):
#        pass

        
    """################################################################################
    ################################################################################
    ################################ SEGUIMIENTO REVISION #########################################
    ################################################################################ 
    ################################################################################"""
    
    def rev_seguimiento(self):
         #Preparo la finestra
        v_seg = tk.Toplevel(self.v) #creo la finestra
        v_seg.geometry("290x200") #defineixo les seves dimensions
        v_seg.title("Tipo de seguimiento") #li fico títol
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.rev_seguimiento_onco, v_seg)
        alta_pac_params2=partial(self.rev_seguimiento_art, v_seg)
        
        # Programar botó
        
        etiq_p= tk.Label(v_seg, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_seg, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_seg,text="Seguimiento oncológico", command = alta_pac_params).grid(column=2,row=2)
        
        etiq_p3= tk.Label(v_seg, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_seg,text="Seguimiento dolor articular", command = alta_pac_params2).grid(column=2,row=6)
        
        #Se pueden añadir más botones al implementar más rutas (muscular, etc)
        
        etiq_p4= tk.Label(v_seg, text= "    ")
        etiq_p4.grid(column=2, row=8) #posicion
        
        btnSortir=tk.Button(v_seg,text="Salir", command = v_seg.destroy).grid(column=2,row=10)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_seg.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_seg.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_seg)
     
    def rev_seguimiento_art(self, v_seg):
        #Preparo la finestra
        v_tipo = tk.Toplevel(self.v) #creo la finestra
        v_tipo.geometry("275x210") #defineixo les seves dimensions
        v_tipo.title("Dolor articular") #li fico títol
        
        etiq_p= tk.Label(v_tipo, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        
        # Tipo (desplegable)
        etiq_t = tk.Label(v_tipo, text= "Tipo:")
        etiq_t.grid(column=1, row=2)
        tipos = ['Sin sospechas','Sosp. enf reumatológica','Sospecha de infección']
        spin_t = ttk.Combobox(v_tipo, values=tipos, state="readonly")
        spin_t.grid(column=2, row=2)
        
        etiq_p= tk.Label(v_tipo, text= "    ")
        etiq_p.grid(column=1, row=3) #posicion
        
        # Zona (desplegable)
        etiq_z = tk.Label(v_tipo, text= "Zona:")
        etiq_z.grid(column=1, row=4)
        zonas = ['Rodilla']
#        zonas = ['Hombro','Codo','Mano y muñeca','Cadera','Articulaciones sacroilíacas','Rodilla','Tobillo y pie','Columna cervical','Columna dorsal y lumbar','Estenosis de canal','Escoliosis']
        spin_z = ttk.Combobox(v_tipo, values=zonas, state="readonly")
        spin_z.grid(column=2, row=4)
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.rev_seg_zonas, spin_t, spin_z, v_tipo, v_seg)
        
        etiq_p= tk.Label(v_tipo, text= "    ")
        etiq_p.grid(column=1, row=6) #posicion
        btnAsignar3=tk.Button(v_tipo,text="Continuar", command = alta_pac_params).grid(column=2,row=8)
        
        btnSortir=tk.Button(v_tipo,text="Atrás", command = v_tipo.destroy).grid(column=1,row=8)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_tipo.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_tipo.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_tipo)
    
    def rev_seg_zonas(self, extra, zona, v_tipo, v_seg):
        if zona.get() == 'Rodilla':
             #Preparo la finestra
            v_rod = tk.Toplevel(self.v) #creo la finestra
            v_rod.geometry("600x300") #defineixo les seves dimensions
            v_rod.title("Escenarios clínicos") #li fico títol
            
            
            # de la llibreria functools
            # assignar parcial per a funció, per a poder assignar directament command amb variables
            #accedim al métode auxiliar
            alta_pac_params=partial(self.seg_rod_trauma, extra, v_rod, v_tipo, v_seg)
            alta_pac_params2=partial(self.seg_rod_uso, extra, v_rod, v_tipo, v_seg)
            alta_pac_params3=partial(self.seg_rod_quiru, extra, v_rod, v_tipo, v_seg)
            ruta=None
            v_r=None
            v_p=None
            alta_pac_params4=partial(self.seg_rod_ines,ruta,extra,v_r,v_p, v_rod, v_tipo, v_seg)
            alta_pac_params5=partial(self.seg_bultoma, extra, v_rod, v_tipo, v_seg)            
            
            # Programar botó
            etiq_p= tk.Label(v_rod, text= "    ")
            etiq_p.grid(column=0, row=0) #posicion
            etiq_p2= tk.Label(v_rod, text= "    ")
            etiq_p2.grid(column=2, row=0) #posicion
            btnAsignar=tk.Button(v_rod,text="Dolor agudo traumático", command = alta_pac_params).grid(column=2,row=2)
            
    
            etiq_p3= tk.Label(v_rod, text= "    ")
            etiq_p3.grid(column=2, row=4) #posicion
            
            btnAsignar2=tk.Button(v_rod,text="Dolor agudo/crónico NO traumático o por sobreuso", command = alta_pac_params2).grid(column=2,row=6)
            
            etiq_p4= tk.Label(v_rod, text= "    ")
            etiq_p4.grid(column=2, row=8) #posicion
            
            btnAsignar3=tk.Button(v_rod,text="Dolor postquirúrgico", command = alta_pac_params3).grid(column=2,row=10)
            
            etiq_p5= tk.Label(v_rod, text= "    ")
            etiq_p5.grid(column=2, row=12) #posicion
            
            btnAsignar4=tk.Button(v_rod,text="Dolor inespecífico", command = alta_pac_params4).grid(column=2,row=14)
            
            etiq_p5= tk.Label(v_rod, text= "    ")
            etiq_p5.grid(column=2, row=16) #posicion
            
            btnAsignar4=tk.Button(v_rod,text="Bultoma", command = alta_pac_params5).grid(column=2,row=18)
            
            etiq_p5= tk.Label(v_rod, text= "    ")
            etiq_p5.grid(column=2, row=20) #posicion
            
            btnSortir=tk.Button(v_rod,text="Atrás", command = v_rod.destroy).grid(column=2,row=22)
    
            # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
            v_rod.transient()
    
            #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
            v_rod.grab_set()
    
            # Wait for the window to end
            self.v.wait_window(v_rod)
            
    def seg_bultoma(self, extra, v_rod, v_tipo, v_seg):
        v_rod.destroy()
        v_tipo.destroy()
        messagebox.showinfo(title='Redirección', message='Ha sido redirigido a seguimiento ONCOLÓGICO, es imprescindible haber realizado RX en dos proyecciones, en caso contrario acceder a Solicitud  > Primera visita > Sospecha de tumor.\n\nSi ya ha realizado RX, sleccione una opción según el estado del diagnóstico y de la patología.')      
        self.rev_seguimiento_onco(v_seg)
        
    def seg_rod_trauma(self, extra, v_rod, v_tipo, v_seg):
        #Preparo la finestra
        v_diag = tk.Toplevel(self.v) #creo la finestra
        v_diag.geometry("770x400") #defineixo les seves dimensions
        v_diag.title("Resultado RX") #li fico títol
        
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.negativa, extra, v_diag, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.fractura, extra, v_diag, v_rod, v_tipo, v_seg)
        alta_pac_params3=partial(self.daño_interno, extra, v_diag, v_rod, v_tipo, v_seg)        
        alta_pac_params4=partial(self.luxacion, extra, v_diag, v_rod, v_tipo, v_seg)
        alta_pac_params5=partial(self.frag_compl, extra, v_diag, v_rod, v_tipo, v_seg)  
        
        # Programar botó
        
        etiq_p= tk.Label(v_diag, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_diag, text= "    ")
        etiq_p2.grid(column=1, row=0) #posicion
        etiq_p= tk.Label(v_diag, text= "INFO IMPORTANTE: Para seguir en esta sección es imprescindible haber realizado previamnete una RX AP y lateral en descarga.\n\nSi no se ha realizado acceder a Solicitud > Primera visita > Dolor articular > D. agudo traumático")
        etiq_p.grid(column=1, row=1) #posicion
        
        etiq_p2= tk.Label(v_diag, text= "    ")
        etiq_p2.grid(column=1, row=2) #posicion
        
        btnAsignar=tk.Button(v_diag,text="RX negativa", command = alta_pac_params).grid(column=1,row=3)
        

        etiq_p3= tk.Label(v_diag, text= "    ")
        etiq_p3.grid(column=1, row=4) #posicion
        
        btnAsignar2=tk.Button(v_diag,text="Fractura / lesión osteocondral / derrame", command = alta_pac_params2).grid(column=1,row=6)
        
        etiq_p4= tk.Label(v_diag, text= "    ")
        etiq_p4.grid(column=1, row=8) #posicion
        
        btnAsignar3=tk.Button(v_diag,text="Daño interno adicional: lesión meniscal, LCA, LCP", command = alta_pac_params3).grid(column=1,row=14)
        
        etiq_p5= tk.Label(v_diag, text= "    ")
        etiq_p5.grid(column=1, row=16) #posicion
        
        btnAsignar4=tk.Button(v_diag,text="Luxación rodilla / rótula", command = alta_pac_params4).grid(column=1,row=18)
        
        etiq_p6= tk.Label(v_diag, text= "    ")
        etiq_p6.grid(column=1, row=20) #posicion
        
        btnAsignar5=tk.Button(v_diag,text="Fractura compleja / análisis calcificación / \n fragmento osteocondral / mapa óseo prequirúrgico", command = alta_pac_params5).grid(column=1,row=22)
        
        etiq_p7= tk.Label(v_diag, text= "    ")
        etiq_p7.grid(column=1, row=24) #posicion
        
        btnSortir=tk.Button(v_diag,text="Atrás", command = v_diag.destroy).grid(column=1,row=26)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_diag.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_diag.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_diag)
    
    def negativa(self, extra, v_diag, v_rod, v_tipo, v_seg):
        ruta='R1'
        v_t=None
        subt='Negativa'
        self.seg_trata(ruta, extra, subt, v_t, v_diag, v_rod, v_tipo, v_seg)
        
    def fractura(self, extra, v_diag, v_rod, v_tipo, v_seg):
        ruta='R2'
        v_t = tk.Toplevel(self.v)
        v_t.geometry("450x250")
        v_t.title("Seleccionar") 
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_t = tk.Label(v_t, text= "Seleccionar resultado RX")
        etiq_t.grid(column=2, row=2)
        op = ['Fractura','Lesión osteocondral','Derrame']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=4, row=2)
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.seg_trata,ruta, extra, spin_t, v_t, v_diag, v_rod, v_tipo, v_seg)
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=6) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=8)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=8) #boton salir: se cierra la ventana
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=10) #posicion


        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)
    
    def seg_trata(self,ruta, extra, subt, v_t, v_diag, v_rod, v_tipo, v_seg):
        v_so = tk.Toplevel(self.v)
        v_so.geometry("400x250")
        v_so.title("TTO") 
        
        etiq_p= tk.Label(v_so, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_so, text= "¿Se le ha aplicado tratamiento al paciente?")
        etiq_p.grid(column=2, row=2) #posicion

        v_m=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_seg_rod,ruta, extra, subt, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.seg_mej_rod,ruta, extra, subt, v_so, v_t, v_diag, v_rod, v_tipo, v_seg)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_so,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_so,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
    
    def seg_mej_rod(self, ruta, extra, subt, v_so, v_t, v_diag, v_rod, v_tipo, v_seg):
        if ruta == 'R2':
            ruta='R2PT'
        if ruta == 'R1':
            ruta='R1PT'
            
        v_m = tk.Toplevel(self.v)
        v_m.geometry("350x250")
        v_m.title("TTO") 
        
        etiq_p= tk.Label(v_m, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_m, text= "Respuesta al tratamiento")
        etiq_p.grid(column=2, row=2) #posicion
        
        sos=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_seg_rod, ruta, extra, subt, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.sol_seg_rm_rod, ruta, extra, subt, sos, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg)
        
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_m,text="Mejoría", command = alta_pac_params).grid(column=2,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        btnAsignar2=tk.Button(v_m,text="No mejoría o nuevos signos de alarma", command = alta_pac_params2).grid(column=2,row=10)
        
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=12) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_m,text="Atrás", command = v_m.destroy).grid(column=2,row=14) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_m.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_m.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_m)
    
        
    def sol_seg_rod(self, ruta, extra, subt, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg):

        #Preparo la nueva ventana para dar de alta al paciente
        v_sol = tk.Toplevel(self.v)
        v_sol.geometry("650x350")
        v_sol.title("Resumen y guardar") 
        
        if ruta=='R2PT':
            etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: "+subt.get()+'.\nMejoría en respuesta a tratamiento.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Fin del estudio.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            ruta='R2PTN'

        if ruta=='R1PT':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: Negativa.\nMejoría en respuesta a tratamiento.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Fin del estudio.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            ruta='R1PTN'

        if ruta=='R1':
            etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: Negativa.\nPendiente de tratamiento.")
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Aplicar tratamiento.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='R2':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: '+subt.get()+'.\nPendiente de tratamiento.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Aplicar tratamiento.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)

        
        # DNI
        etiq_dni = tk.Label(v_sol, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_sol, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        sos=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_seg_rod_aux, e_dni, spin_t, ruta, extra, subt,sos, v_sol, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_sol,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_sol,text="Atrás", command = v_sol.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_sol.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_sol.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_sol)
        
    def sol_seg_rm_rod(self, ruta, extra, subt, sos, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg):
        
        #Preparo la nueva ventana para dar de alta al paciente
        v_sol = tk.Toplevel(self.v)
        v_sol.geometry("650x350")
        v_sol.title("Resumen y guardar") 
        
        if ruta=='R2PT':
            etiq_p= tk.Label(v_sol, text= "Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: "+subt.get()+'.\nNo mejoría o nuevos síntomas en respuesta a tratamiento.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)

        if ruta=='R1PT':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: Negativa.\nNo mejoría o nuevos síntomas en respuesta a tratamiento.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='R3':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: daño interno adicional - '+ subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
        
        if ruta=='R4':

            if sos.get() == 'Sí':
                etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: '+ subt.get()+'.\nSospecha de lesión vascular')
                etiq_p.grid(column=0, row=0) #posicion
                # Tipo de prueba de imagen (desplegable)
                etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
                etiq_t.grid(column=0, row=4)
                op = ['RM','TC reconstrucción','Angio-TC']
                spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
                spin_t.grid(column=1, row=4)
            if sos.get() == 'No':
                etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: '+ subt.get())
                etiq_p.grid(column=0, row=0) #posicion
                # Tipo de prueba de imagen (desplegable)
                etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
                etiq_t.grid(column=0, row=4)
                op = ['RM','TC reconstrucción']
                spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
                spin_t.grid(column=1, row=4)
        
        if ruta=='R5':
            
            if sos.get() == 'Sí':
                etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: '+ subt.get()+'.\nSospecha de lesión vascular')
                etiq_p.grid(column=0, row=0) #posicion
                # Tipo de prueba de imagen (desplegable)
                etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
                etiq_t.grid(column=0, row=4)
                op = ['TC reconstrucción','Angio-TC']
                spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
                spin_t.grid(column=1, row=4)
            if sos.get() == 'No':
                etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor agudo traumático de rodilla. Solución RX: '+ subt.get())
                etiq_p.grid(column=0, row=0) #posicion
                # Tipo de prueba de imagen (desplegable)
                etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
                etiq_t.grid(column=0, row=4)
                op = ['TC reconstrucción']
                spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
                spin_t.grid(column=1, row=4)


        # DNI
        etiq_dni = tk.Label(v_sol, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_sol, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_seg_rod_aux, e_dni, spin_t, ruta, extra, subt, sos, v_sol, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_sol,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_sol,text="Atrás", command = v_sol.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_sol.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_sol.grab_set()
        
    def sol_seg_rod_aux(self, dni, tipo, ruta, extra, subt, sos, v_sol, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([dni.get(),tipo.get()]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
            messagebox.showinfo(title='Paciente no existente', message='El paciente con este número de historial clínico no existe')

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)

            self.h.seg_rodi(dni.get(),tipo.get(),ruta,extra,subt,sos)
            
            messagebox.showinfo(title='Guardado', message='Diagnóstico guardado') #muestro confirmacion de que el paciente se ha añadido
            messagebox.showinfo(title='En desarrollo', message='Las siguientes secciones de Citación e Informes se desarrollarán en futuras versiones.')                

            v_sol.destroy()
            v_seg.destroy()
            v_tipo.destroy()
            v_rod.destroy()
            v_diag.destroy()
            if ruta!='R1' and ruta!='R1PTN' and ruta!='R1PT':
                v_t.destroy()
            if ruta!='R3' and ruta!='R4' and ruta!='R5':
                v_so.destroy()
            if ruta!='R1' and ruta!='R2' and ruta!='R3' and ruta!='R4' and ruta!='R5':
                v_m.destroy()
        
    def daño_interno(self, extra, v_diag, v_rod, v_tipo, v_seg):
        ruta='R3'
        v_t = tk.Toplevel(self.v)
        v_t.geometry("450x250")
        v_t.title("Seleccionar") 
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_t = tk.Label(v_t, text= "Seleccionar resultado RX:\ndaño interno adicional")
        etiq_t.grid(column=2, row=2)
        op = ['Lesión meniscal','LCA','LCP']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=4, row=2)
       
        v_m=None
        v_so=None
        sos=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_seg_rm_rod, ruta, extra, spin_t, sos, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg)
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=6) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=8)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=8) #boton salir: se cierra la ventana
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=10) #posicion


        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)
        
    def luxacion(self, extra, v_diag, v_rod, v_tipo, v_seg):
        ruta='R4'
        v_t = tk.Toplevel(self.v)
        v_t.geometry("450x250")
        v_t.title("Seleccionar") 
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_t = tk.Label(v_t, text= "Seleccionar resultado RX")
        etiq_t.grid(column=2, row=2)
        op = ['Luxación rodilla','Luxación rótula']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=4, row=2)
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=6) #posicion
                
        etiq_s = tk.Label(v_t, text= "¿Hay sospecha de lesión vascular?")
        etiq_s.grid(column=2, row=8)
        op = ['Sí','No']
        spin_s = ttk.Combobox(v_t, values=op, state="readonly")
        spin_s.grid(column=4, row=8)
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=10) #posicion    
        v_m=None
        v_so=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_seg_rm_rod, ruta, extra, spin_t, spin_s, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg)
        

        
        # Programar botó
        btnAsignar=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=12)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=12) #boton salir: se cierra la ventana
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=14) #posicion


        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)
        
    def frag_compl(self, extra, v_diag, v_rod, v_tipo, v_seg):
        ruta='R5'
        v_t = tk.Toplevel(self.v)
        v_t.geometry("450x250")
        v_t.title("Seleccionar") 
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_t = tk.Label(v_t, text= "Seleccionar resultado RX")
        etiq_t.grid(column=2, row=2)
        op = ['Fractura compleja','Análisis calcificaciones','Fragmento osteocondral','Mapa óseo prequirúrgico']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=4, row=2)

        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=6) #posicion
                
        etiq_s = tk.Label(v_t, text= "¿Hay sospecha de lesión vascular?")
        etiq_s.grid(column=2, row=8)
        op = ['Sí','No']
        spin_s = ttk.Combobox(v_t, values=op, state="readonly")
        spin_s.grid(column=4, row=8)
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=10) #posicion
        
        v_m=None
        v_so=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_seg_rm_rod, ruta, extra, spin_t, spin_s, v_m, v_so, v_t, v_diag, v_rod, v_tipo, v_seg)
        

        # Programar botó
        btnAsignar=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=12)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=12) #boton salir: se cierra la ventana
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=14) #posicion


        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)
    
    
    def seg_rod_uso(self, extra, v_rod, v_tipo, v_seg):
        #Preparo la finestra
        v_p = tk.Toplevel(self.v) #creo la finestra
        v_p.geometry("390x400") #defineixo les seves dimensions
        v_p.title("Tipo de dolor y diagnóstico") #li fico títol
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.dif_seg, extra, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.dif_du, extra, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params3=partial(self.fem_seg, extra, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params4=partial(self.fem_in, extra, v_p, v_rod, v_tipo, v_seg)
        # Programar botó
        
        etiq_p= tk.Label(v_p, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_p, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_p,text="Difuso - diagnóstico seguro", command = alta_pac_params).grid(column=2,row=2)
        
        etiq_p3= tk.Label(v_p, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_p,text="Difuso - diagnóstico dudoso", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p3= tk.Label(v_p, text= "    ")
        etiq_p3.grid(column=2, row=8) #posicion
        
        btnAsignar2=tk.Button(v_p,text="Femoro-patelar - diagnóstico seguro", command = alta_pac_params3).grid(column=2,row=10)
        
        etiq_p3= tk.Label(v_p, text= "    ")
        etiq_p3.grid(column=2, row=12) #posicion
        
        btnAsignar2=tk.Button(v_p,text="Femoro-patelar - inestabilidad", command = alta_pac_params4).grid(column=2,row=14)
        
        etiq_p4= tk.Label(v_p, text= "    ")
        etiq_p4.grid(column=2, row=16) #posicion
        
        btnSortir=tk.Button(v_p,text="Atrás", command = v_p.destroy).grid(column=2,row=18)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_p.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_p.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_p)        
    
    def dif_du(self,extra, v_p, v_rod, v_tipo, v_seg):
        ruta='d_du'
        self.reuma(ruta, extra, v_p, v_rod, v_tipo, v_seg)
        
    def reuma(self, ruta, extra, v_p, v_rod, v_tipo, v_seg):

        v_r = tk.Toplevel(self.v)
        v_r.geometry("400x250")
        v_r.title("Reumático") 
        
        etiq_p= tk.Label(v_r, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_r, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_r, text= "¿Se diagnostica dolor REUMÁTICO?")
        etiq_p.grid(column=2, row=2) #posicion

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.tipo, ruta, extra, v_r, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.seg_rod_ines, ruta, extra, v_r, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p2= tk.Label(v_r, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_r,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_r,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_r, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_r,text="Atrás", command = v_r.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_r.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_r.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_r)
        
        
    def tipo(self, ruta, extra, v_r, v_p, v_rod, v_tipo, v_seg):
        #Preparo la finestra
        v_t = tk.Toplevel(self.v) #creo la finestra
        v_t.geometry("390x230") #defineixo les seves dimensions
        v_t.title("Tipo de dolor y diagnóstico") #li fico títol

        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion

        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_t, text= "Tipo de patología")
        etiq_t.grid(column=2, row=2)
        op = ['Lesión LLI','Lesión LLE', 'Patología tendinosa','Sinovitis','Bursitis','Meniscopatía','Lesión LCA', 'Lesión LCP','Lesiones osteocondrales']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=3, row=2)
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.presol_seg_uso, ruta, extra, spin_t, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=2, row=3) #posicion
        
        btnAsi=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=4)
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=4)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)  

    def dif_seg(self,extra, v_p, v_rod, v_tipo, v_seg):
        ruta='d_seg'
        self.preg_tto(ruta, extra, v_p, v_rod, v_tipo, v_seg)
        
    def fem_seg(self,extra, v_p, v_rod, v_tipo, v_seg):
        ruta='f_seg'
        self.preg_tto(ruta, extra, v_p, v_rod, v_tipo, v_seg)
        
    def fem_in(self,extra, v_p, v_rod, v_tipo, v_seg):
        ruta='f_in'
        self.preg_tto(ruta, extra, v_p, v_rod, v_tipo, v_seg)
    
    def preg_tto(self, ruta, extra, v_p, v_rod, v_tipo, v_seg):
        v_so = tk.Toplevel(self.v)
        v_so.geometry("400x250")
        v_so.title("TTO") 
        
        etiq_p= tk.Label(v_so, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_so, text= "¿Se le ha aplicado tratamiento al paciente?")
        etiq_p.grid(column=2, row=2) #posicion
        
        sub_tip=None
        v_t=None
        v_e=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.ap_tto, ruta, extra, sub_tip, v_e, v_t, v_so, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.dudas_uso, ruta, extra, sub_tip, v_e, v_t, v_so, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_so,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_so,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)

    def ap_tto(self, ruta, extra, sub_tip, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg):
        if ruta=='d_seg':
            ruta='d_seg_tto'
            v_d=None
            self.sol_seg_uso(ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
        if ruta=='f_seg':
            ruta='f_seg_tto'
            v_d=None
            self.sol_seg_uso(ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
        if ruta=='f_in':
            ruta='f_in_tto'
            v_d=None
            self.sol_seg_uso(ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
            
    def presol_seg_uso(self, ruta, extra, sub_tip, v_t, v_r, v_p, v_rod, v_tipo, v_seg):
        if sub_tip.get() == 'Lesión LLI' or sub_tip.get() =='Lesión LLE' or sub_tip.get() == 'Patología tendinosa' or sub_tip.get() =='Sinovitis' or sub_tip.get() =='Bursitis':
            v_e = tk.Toplevel(self.v)
            v_e.geometry("400x250")
            v_e.title("ECO") 
            
            etiq_p= tk.Label(v_e, text= "    ")
            etiq_p.grid(column=0, row=0) #posicion
            etiq_p2= tk.Label(v_e, text= "    ")
            etiq_p2.grid(column=2, row=0) #posicion
            
            etiq_p= tk.Label(v_e, text= "¿Se ha realizado ECOGRAFÍA?")
            etiq_p.grid(column=2, row=2) #posicion
    
            # de la llibreria functools
            # assignar parcial per a funció, per a poder assignar directament command amb variables
            alta_pac_params=partial(self.eco_uso, ruta, extra, sub_tip, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
            alta_pac_params2=partial(self.dudas_uso, ruta, extra, sub_tip, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
            
            etiq_p2= tk.Label(v_e, text= "    ")
            etiq_p2.grid(column=2, row=4) #posicion
            
            # Programar botó
            btnAsignar=tk.Button(v_e,text="No", command = alta_pac_params).grid(column=3,row=6)
            #con el boton continuar se manda al metodo alta_pac_aux
            btnAsignar2=tk.Button(v_e,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
            
            etiq_p2= tk.Label(v_e, text= "    ")
            etiq_p2.grid(column=2, row=8) #posicion
            
            #con el boton continuar se manda al metodo alta_pac_aux
            btnSortir=tk.Button(v_e,text="Atrás", command = v_e.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana
    
            # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
            v_e.transient()
    
            #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
            v_e.grab_set()
    
            # Wait for the window to end
            self.v.wait_window(v_e)
        
        else:
            v_e=None
            v_d=None
            self.sol_seg_uso(ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
    
    def eco_uso(self, ruta, extra, sub_tip, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg):   
        ruta='eco_d_du'
        v_d=None
        self.sol_seg_uso(ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)        
        
    def dudas_uso(self, ruta, extra, sub_tip, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg):       
        v_d = tk.Toplevel(self.v)
        v_d.geometry("400x250")
        v_d.title("Dudas") 
        
        etiq_p= tk.Label(v_d, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_d, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        if ruta=='d_du' or 'd_seg' or 'f_seg':
            etiq_p= tk.Label(v_d, text= "¿Hay dudas o persistencia de dolor?")
            etiq_p.grid(column=2, row=2) #posicion
        if ruta=='f_in':
            etiq_p= tk.Label(v_d, text= "¿No mejoría o estudio prequirúrgico?")
            etiq_p.grid(column=2, row=2) #posicion            

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.fin_uso, ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.sol_seg_uso, ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p2= tk.Label(v_d, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_d,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_d,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_d, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_d,text="Atrás", command = v_d.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_d.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_d.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_d)
        
    def fin_uso(self, ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg):    
        if ruta=='d_du':
            ruta='d_du_fin'
        if ruta=='d_seg':
            ruta='d_seg_fin'
        if ruta=='f_seg':
            ruta='f_seg_fin'
        if ruta=='f_in':
            ruta='f_in_fin'
        self.sol_seg_uso(ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)
    
    def sol_seg_uso(self, ruta, extra, sub_tip, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg):
        #Preparo la nueva ventana para dar de alta al paciente
        v_sol = tk.Toplevel(self.v)
        v_sol.geometry("650x350")
        v_sol.title("Resumen y guardar") 
        
        if ruta=='d_du_fin':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso: '+sub_tip.get()+'. Tratado con éxito.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Fin del estudio']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)

        if ruta=='d_seg_fin':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso tratado con éxito.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Fin del estudio']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='f_seg_fin':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor femoro-patelar tratado con éxito.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Fin del estudio']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='f_in_fin':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor femoro-patelar con inestabilidad tratado con éxito.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Fin del estudio']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='eco_d_du':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso: '+sub_tip.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['ECO']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='d_seg_tto':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso pendiente de tratamiento')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Pendiente de tratamiento.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)   
            
        if ruta=='f_seg_tto':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor femoro-patelar pendiente de tratamiento')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Pendiente de tratamiento.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)

        if ruta=='f_in_tto':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor femoro-patelar con inestabilidad pendiente de tratamiento')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Pendiente de tratamiento.']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='d_seg':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso persistente o con dudas.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='d_du':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso: '+sub_tip.get()+'. Persistente o con dudas.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='f_seg':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor femoro-patelar persistente o con dudas.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='f_in':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor femoro-patelar con inestabilidad. Sin mejoría o en estudio prequirúrgico.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['TC dinámico']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)     
                
        # DNI
        etiq_dni = tk.Label(v_sol, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_sol, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_seg_uso_aux, e_dni, spin_t, ruta, extra, sub_tip, v_sol, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_sol,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_sol,text="Atrás", command = v_sol.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_sol.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_sol.grab_set()
        
    def sol_seg_uso_aux(self, dni, tipo, ruta, extra, sub_tip, v_sol, v_d, v_e, v_t, v_r, v_p, v_rod, v_tipo, v_seg):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([dni.get(),tipo.get()]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
            messagebox.showinfo(title='Paciente no existente', message='El paciente con este número de historial clíncico no existe')

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)
            sos=None
            self.h.seg_rodi(dni.get(),tipo.get(),ruta,extra,sub_tip,sos)
            
            messagebox.showinfo(title='Guardado', message='Diagnóstico guardado') #muestro confirmacion de que el paciente se ha añadido
            messagebox.showinfo(title='En desarrollo', message='Las siguientes secciones de Citación e Informes se desarrollarán en futuras versiones.')                

            v_sol.destroy()
            v_seg.destroy()
            v_tipo.destroy()
            v_rod.destroy()
            v_p.destroy()
            v_r.destroy()
            try:
                v_d.destroy()
            except AttributeError:
                pass            
            try:
                v_e.destroy()
            except AttributeError:
                pass            
            try:
                v_t.destroy()
#            if ruta!='d_seg_tto' and ruta!='f_seg_tto' and ruta!='f_in_tto' and ruta!='eco_d_du' and ruta!='d_du':
#                v_d.destroy()
#            if ruta!='d_seg' and ruta!='d_du_fin' and ruta!='f_seg_fin' and ruta!='f_seg' and ruta!='f_in' and ruta!='f_in_fin':
#                v_e.destroy()
#            if ruta!='d_seg' and ruta!='d_du_fin' and ruta!='f_seg_fin' and ruta!='f_seg' and ruta!='f_in' and ruta!='f_in_fin':
#                v_t.destroy()
#            try:
#                if ruta!='d_du' and sub_tip.get()=='Meniscopatía':
#                    v_e.destroy()
#                if ruta!='d_du' and sub_tip.get()=='Lesión LCA':
#                    v_e.destroy()
#                if ruta!='d_du' and sub_tip.get()=='Lesión LCP':
#                    v_e.destroy()
#                if ruta!='d_du' and sub_tip.get()=='Lesiones osteocondrales':
#                    v_e.destroy()
            except AttributeError:
                pass
    def seg_rod_quiru(self, extra, v_rod, v_tipo, v_seg):
        #Preparo la finestra
        v_p = tk.Toplevel(self.v) #creo la finestra
        v_p.geometry("696x390") #defineixo les seves dimensions
        v_p.title("Tipo de lesión") #li fico títol
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.prote, extra, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.menisco, extra, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params3=partial(self.osteoc, extra, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params4=partial(self.lca, extra, v_p, v_rod, v_tipo, v_seg)
        # Programar botó

        etiq_p= tk.Label(v_p, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_p, text= "    ")
        etiq_p2.grid(column=1, row=0) #posicion
        etiq_p= tk.Label(v_p, text= "INFO IMPORTANTE: Para seguir en esta sección es imprescindible haber realizado previamnete una RX AP y Lateral en carga.\n\nSi no se ha realizado acceder a Solicitud > Primera visita > Dolor articular > D. postiquúrgico")
        etiq_p.grid(column=1, row=1) #posicion
                
        etiq_p= tk.Label(v_p, text= "    ")
        etiq_p.grid(column=2, row=2) #posicion
        etiq_p2= tk.Label(v_p, text= "    ")
        etiq_p2.grid(column=1, row=2) #posicion
        btnAsignar=tk.Button(v_p,text="Protésica - aflojamiento", command = alta_pac_params).grid(column=1,row=3)
        
        etiq_p3= tk.Label(v_p, text= "    ")
        etiq_p3.grid(column=1, row=4) #posicion
        
        btnAsignar2=tk.Button(v_p,text="NO protésica - Meniscos", command = alta_pac_params2).grid(column=1,row=6)
        
        etiq_p3= tk.Label(v_p, text= "    ")
        etiq_p3.grid(column=1, row=8) #posicion
        
        btnAsignar2=tk.Button(v_p,text="NO protésica - Lesión osteocondral", command = alta_pac_params3).grid(column=1,row=10)
        
        etiq_p3= tk.Label(v_p, text= "    ")
        etiq_p3.grid(column=1, row=12) #posicion
        
        btnAsignar2=tk.Button(v_p,text="NO protésica - LCA", command = alta_pac_params4).grid(column=1,row=14)
        
        etiq_p4= tk.Label(v_p, text= "    ")
        etiq_p4.grid(column=1, row=16) #posicion
        
        btnSortir=tk.Button(v_p,text="Atrás", command = v_p.destroy).grid(column=1,row=18)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_p.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_p.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_p)
        
    def prote(self, extra, v_rod, v_p, v_tipo, v_seg):
        ruta='prote'
        v_so = tk.Toplevel(self.v)
        v_so.geometry("350x250")
        v_so.title("TC/GAMMAGRAFÍA") 
        
        etiq_p= tk.Label(v_so, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_so, text= "¿Ha realizado ya una TC o GAMMAGRAFÍA al paciente?")
        etiq_p.grid(column=2, row=2) #posicion
        
        v_in=None
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.quiru_sol, ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg)
        alta_pac_params2=partial(self.post_tcgm, ruta, extra, v_so, v_rod, v_p, v_tipo, v_seg)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_so,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_so,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
    
    def post_tcgm(self, ruta, extra, v_so, v_rod, v_p, v_tipo, v_seg):
        #Preparo la finestra
        v_in = tk.Toplevel(self.v) #creo la finestra
        v_in.geometry("290x200") #defineixo les seves dimensions
        v_in.title("Presencia o ausencia de infección") #li fico títol
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.asep_tto, ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg)
        alta_pac_params2=partial(self.sep_biop, ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg)
        
        # Programar botó
        
        etiq_p= tk.Label(v_in, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_in, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_in,text="Aséptica", command = alta_pac_params).grid(column=2,row=2)
        
        etiq_p3= tk.Label(v_in, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_in,text="Séptica", command = alta_pac_params2).grid(column=2,row=6)
        
        #Se pueden añadir más botones al implementar más rutas (muscular, etc)
        
        etiq_p4= tk.Label(v_in, text= "    ")
        etiq_p4.grid(column=2, row=8) #posicion
        
        btnSortir=tk.Button(v_in,text="Atrás", command = v_in.destroy).grid(column=2,row=10)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_in.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_in.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_in)
    
    def asep_tto(self, ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg):
        ruta='p_tto'
        self.quiru_sol(ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg)
    def sep_biop(self, ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg):
        ruta='p_biop'
        self.quiru_sol(ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg)
    def menisco(self, extra, v_p, v_rod, v_tipo, v_seg):
        ruta='meni'
        v_in=None
        v_so=None
        self.quiru_sol(ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg)        
    def osteoc(self, extra, v_p, v_rod, v_tipo, v_seg):
        ruta='osteo'
        v_in=None
        v_so=None
        self.quiru_sol(ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg) 
    def lca(self, extra, v_p, v_rod, v_tipo, v_seg):    
        ruta='lca'
        v_in=None
        v_so=None
        self.quiru_sol(ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg) 
        
    def quiru_sol(self,ruta, extra, v_in, v_so, v_rod, v_p, v_tipo, v_seg):   
        #Preparo la nueva ventana para dar de alta al paciente
        v_sol = tk.Toplevel(self.v)
        v_sol.geometry("650x350")
        v_sol.title("Resumen y guardar") 
        
        if ruta=='lca':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla postquirúrgico. Lesión no protésica: LCA')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)

        if ruta=='osteo':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla postquirúrgico. Lesión no protésica: osteocondral')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='meni':
            etiq_p= tk.Label(v_sol, text= 'INFO IMPORTANTE: Se recomienda valorar punción, aspiración y análisis de líquidos.\n\nResumen del diagnóstico:\n    Dolor de rodilla postquirúrgico. Lesión no protésica: meniscos')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RM', 'Artro-RM (si dudas)','Artro-TC (si dudas)']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='p_tto':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla postquirúrgico.\nLesión protésica: aflojamiento con causa aséptica.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Pendiente de tratamiento']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='p_biop':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla postquirúrgico.\nLesión protésica: aflojamiento con causa séptica.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['No pruebas de imagen indicadas. Realizar punción y aspiración']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='prote':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla postquirúrgico.\nLesión protésica: aflojamiento.')
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['TC','Gammagrafía ósea', 'Gammagrafía leucocitos autólogos']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)       
                 
        # DNI
        etiq_dni = tk.Label(v_sol, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_sol, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.quiru_sol_aux, e_dni, spin_t, ruta, extra, v_sol, v_in, v_so, v_rod, v_p, v_tipo, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_sol,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_sol,text="Atrás", command = v_sol.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_sol.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_sol.grab_set()
        
    def quiru_sol_aux(self, dni, tipo, ruta, extra, v_sol, v_in, v_so, v_rod, v_p, v_tipo, v_seg):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([dni.get(),tipo.get()]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
            messagebox.showinfo(title='Paciente no existente', message='El paciente con este número de historial clíncico no existe')

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)

            self.h.rodi(dni.get(),tipo.get(),ruta,extra)
            
            messagebox.showinfo(title='Guardado', message='Diagnóstico guardado') #muestro confirmacion de que el paciente se ha añadido
            messagebox.showinfo(title='En desarrollo', message='Las siguientes secciones de Citación e Informes se desarrollarán en futuras versiones.')                

            v_sol.destroy()
            v_seg.destroy()
            v_tipo.destroy()
            v_rod.destroy()
            v_p.destroy()
            if ruta!='lca' and ruta!='osteo' and ruta!='meni' and ruta!='prote':
                v_in.destroy()
            if ruta!='lca' and ruta!='osteo' and ruta!='meni':
                v_so.destroy()

  
    def seg_rod_ines(self, ruta, extra, v_r, v_p, v_rod, v_tipo, v_seg):
         #Preparo la finestra
        v_d = tk.Toplevel(self.v) #creo la finestra
        v_d.geometry("290x200") #defineixo les seves dimensions
        v_d.title("Presencia o no de derrame") #li fico títol
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.derrame, ruta, extra, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.no_derrame, ruta, extra, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        
        # Programar botó
        
        etiq_p= tk.Label(v_d, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_d, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_d,text="Derrame", command = alta_pac_params).grid(column=2,row=2)
        
        etiq_p3= tk.Label(v_d, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_d,text="NO derrame", command = alta_pac_params2).grid(column=2,row=6)
        
        #Se pueden añadir más botones al implementar más rutas (muscular, etc)
        
        etiq_p4= tk.Label(v_d, text= "    ")
        etiq_p4.grid(column=2, row=8) #posicion
        
        btnSortir=tk.Button(v_d,text="Atrás", command = v_d.destroy).grid(column=2,row=10)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_d.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_d.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_d)

    def derrame(self, ruta, extra, v_d, v_r, v_p, v_rod, v_tipo, v_seg):
         #Preparo la finestra
        v_mz = tk.Toplevel(self.v) #creo la finestra
        v_mz.geometry("290x300") #defineixo les seves dimensions
        v_mz.title("Empeoramiento con actividad") #li fico títol
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.mecanico, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.no_mecanico, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        
        # Programar botó
        
        etiq_p= tk.Label(v_mz, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_mz, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_mz,text="Mecánico: empeora con actividad", command = alta_pac_params).grid(column=2,row=2)
        
        etiq_p3= tk.Label(v_mz, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_mz,text="NO mecánico: no empeora con actividad", command = alta_pac_params2).grid(column=2,row=6)
        
        #Se pueden añadir más botones al implementar más rutas (muscular, etc)
        
        etiq_p4= tk.Label(v_mz, text= "    ")
        etiq_p4.grid(column=2, row=8) #posicion
        
        btnSortir=tk.Button(v_mz,text="Atrás", command = v_mz.destroy).grid(column=2,row=10)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_mz.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_mz.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_mz)
    
    def mecanico(self, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg):
        if ruta=='d_du':
            ruta='l_mec'
        else:
            ruta='mec'
        #Preparo la finestra
        v_t = tk.Toplevel(self.v) #creo la finestra
        v_t.geometry("390x230") #defineixo les seves dimensions
        v_t.title("Diagnóstico") #li fico títol

        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion

        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_t, text= "Tipo de patología")
        etiq_t.grid(column=2, row=2)
        op = ['Lesión osteocondral','Artrosis']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=3, row=2)
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.sol_ines, ruta, extra, spin_t, v_t, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=2, row=3) #posicion
        
        btnAsi=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=4)
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=4)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)  

    def no_mecanico(self, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg):
        if ruta=='d_du':
            ruta='l_Nmec'
        else:
            ruta='Nmec'
        #Preparo la finestra
        v_t = tk.Toplevel(self.v) #creo la finestra
        v_t.geometry("390x230") #defineixo les seves dimensions
        v_t.title("Diagnóstico") #li fico títol

        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion

        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_t, text= "Tipo de patología")
        etiq_t.grid(column=2, row=2)
        op = ['Astropatías cristales','Artritis infecciosa','Enf. reumática sistémica']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=3, row=2)
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.sol_ines, ruta, extra, spin_t, v_t, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=2, row=3) #posicion
        
        btnAsi=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=4)
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=4)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)  
        
    def no_derrame(self, ruta, extra, v_d, v_r, v_p, v_rod, v_tipo, v_seg):
        v_mz = tk.Toplevel(self.v) #creo la finestra
        v_mz.geometry("390x400") #defineixo les seves dimensions
        v_mz.title("Localización del dolor") #li fico títol
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.anterior, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params2=partial(self.medial, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params3=partial(self.lateral, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        alta_pac_params4=partial(self.posterior, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        
        # Programar botó
        etiq_p= tk.Label(v_mz, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_mz, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_mz,text="Anterior", command = alta_pac_params).grid(column=2,row=2)
        
        etiq_p3= tk.Label(v_mz, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_mz,text="Medial", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p3= tk.Label(v_mz, text= "    ")
        etiq_p3.grid(column=2, row=8) #posicion
        
        btnAsignar3=tk.Button(v_mz,text="Lateral", command = alta_pac_params3).grid(column=2,row=10)
        
        etiq_p3= tk.Label(v_mz, text= "    ")
        etiq_p3.grid(column=2, row=12) #posicion
        
        btnAsignar4=tk.Button(v_mz,text="Posterior", command = alta_pac_params4).grid(column=2,row=14)
        
        etiq_p4= tk.Label(v_mz, text= "    ")
        etiq_p4.grid(column=2, row=16) #posicion
        
        btnSortir=tk.Button(v_mz,text="Atrás", command = v_mz.destroy).grid(column=2,row=18)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_mz.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_mz.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_mz)

    def anterior(self, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg):
        if ruta=='d_du':
            ruta='l_ant'
        else:
            ruta='ant'
        #Preparo la finestra
        v_t = tk.Toplevel(self.v) #creo la finestra
        v_t.geometry("390x230") #defineixo les seves dimensions
        v_t.title("Diagnóstico zona anterior") #li fico títol

        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion

        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_t, text= "Tipo de patología")
        etiq_t.grid(column=2, row=2)
        op = ['Tendón cuádriceps','Tendón rotuliano','Bursitis pre/infrapatelar','Síndrome Hoffa','Síndrome Pica','Luxación rótula','Condromalacia rotuliana','Inestabilidad rotuliana']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=3, row=2)
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.sol_ines, ruta, extra, spin_t, v_t, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=2, row=3) #posicion
        
        btnAsi=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=4)
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=4)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)
        
    def medial(self, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg):
        if ruta=='d_du':
            ruta='l_med'
        else:
            ruta='med'
        #Preparo la finestra
        v_t = tk.Toplevel(self.v) #creo la finestra
        v_t.geometry("390x230") #defineixo les seves dimensions
        v_t.title("Diagnóstico zona medial") #li fico títol

        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion

        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_t, text= "Tipo de patología")
        etiq_t.grid(column=2, row=2)
        op = ['Bursitis anserina','Tendinosis anserina','LCM','Nervio safeno','Meniscopatía degenerativa']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=3, row=2)
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.sol_ines, ruta, extra, spin_t, v_t, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=2, row=3) #posicion
        
        btnAsi=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=4)
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=4)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)

    def lateral(self, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg):
        if ruta=='d_du':
            ruta='l_lat'
        else:
            ruta='lat'
        #Preparo la finestra
        v_t = tk.Toplevel(self.v) #creo la finestra
        v_t.geometry("390x230") #defineixo les seves dimensions
        v_t.title("Diagnóstico zona lateral") #li fico títol

        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion

        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_t, text= "Tipo de patología")
        etiq_t.grid(column=2, row=2)
        op = ['Banda iliotibial','Tendinosis biceps','LLE','Nervio CPE','Meniscopatía degenerativa']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=3, row=2)
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.sol_ines, ruta, extra, spin_t, v_t, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=2, row=3) #posicion
        
        btnAsi=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=4)
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=4)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)

    def posterior(self, ruta, extra, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg):
        if ruta=='d_du':
            ruta='l_pos'
        else:
            ruta='pos'
        #Preparo la finestra
        v_t = tk.Toplevel(self.v) #creo la finestra
        v_t.geometry("390x230") #defineixo les seves dimensions
        v_t.title("Diagnóstico zona posterior") #li fico títol

        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion

        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_t, text= "Tipo de patología")
        etiq_t.grid(column=2, row=2)
        op = ['Quiste de Baker','Tendinosis poplíteo','Aneurisma A. poplítea','Atrapamiento A.poplítea']
        spin_t = ttk.Combobox(v_t, values=op, state="readonly")
        spin_t.grid(column=3, row=2)
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.sol_ines, ruta, extra, spin_t, v_t, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=2, row=3) #posicion
        
        btnAsi=tk.Button(v_t,text="Continuar", command = alta_pac_params).grid(column=3,row=4)
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=4)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)

    def sol_ines(self, ruta, extra, subt, v_t, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg):   
        #Preparo la nueva ventana para dar de alta al paciente
        v_sol = tk.Toplevel(self.v)
        v_sol.geometry("650x350")
        v_sol.title("Resumen y guardar") 

        if ruta=='mec':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla inespecífico. Derrame, mecánico. '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RX','RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)

        if ruta=='Nmec':
            if subt.get()!='Enf. reumática sistémica':
                etiq_p= tk.Label(v_sol, text= 'INFO IMPORTANTE: Se recomienda valorar punción, aspiración y análisis de líquidos.\n\nResumen del diagnóstico:\n    Dolor de rodilla inespecífico. Derrame, NO mecánico. '+subt.get())
            else:
                etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla inespecífico. Derrame, NO mecánico. '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RX', 'ECO','RM','Dual TC']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='ant':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla inespecífico. NO derrame, zona anterior: '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            if subt.get()=='Tendón cuádriceps' or subt.get()=='Tendón rotuliano' or subt.get()=='Bursitis pre/infrapatelar':
                op = ['ECO']
            if subt.get()=='Síndrome Hoffa' or subt.get()=='Síndrome Pica' or subt.get()=='Luxación rótula' or subt.get()=='Condromalacia rotuliana':
                op = ['RM']            
            if subt.get()=='Inestabilidad rotuliana':
                op = ['TC']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='med':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla inespecífico. NO derrame, zona medial: '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            if subt.get()=='Meniscopatía degenerativa':
                op = ['RM']
            else:
                op=['ECO']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='lat':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla inespecífico. NO derrame, zona lateral: '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            if subt.get()=='Meniscopatía degenerativa':
                op = ['RM']
            else:
                op=['ECO']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='pos':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla inespecífico. NO derrame, zona posterior: '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            if subt.get()=='Quiste de Baker' or subt.get()=='Tendinosis poplíteo':
                op = ['ECO']
            else:
                op=['ECO','angio-TC']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)       


        if ruta=='l_mec':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso reumático. Derrame, mecánico. '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RX','RM']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)

        if ruta=='l_Nmec':
            if subt.get()!='Enf. reumática sistémica':
                etiq_p= tk.Label(v_sol, text= 'INFO IMPORTANTE: Se recomienda valorar punción, aspiración y análisis de líquidos.\n\nResumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso reumático. Derrame, NO mecánico. '+subt.get())
            else:
                etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso reumático. Derrame, NO mecánico. '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['RX', 'ECO','RM','Dual TC']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='l_ant':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso reumático. NO derrame, zona anterior: '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            if subt.get()=='Tendón cuádriceps' or subt.get()=='Tendón rotuliano' or subt.get()=='Bursitis pre/infrapatelar':
                op = ['ECO']
            if subt.get()=='Síndrome Hoffa' or subt.get()=='Síndrome Pica' or subt.get()=='Luxación rótula' or subt.get()=='Condromalacia rotuliana':
                op = ['RM']            
            if subt.get()=='Inestabilidad rotuliana':
                op = ['TC']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='l_med':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso reumático. NO derrame, zona medial: '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            if subt.get()=='Meniscopatía degenerativa':
                op = ['RM']
            else:
                op=['ECO']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='l_lat':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso reumático. NO derrame, zona lateral: '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            if subt.get()=='Meniscopatía degenerativa':
                op = ['RM']
            else:
                op=['ECO']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta=='l_pos':
            etiq_p= tk.Label(v_sol, text= 'Resumen del diagnóstico:\n    Dolor de rodilla agudo/crónico NO traumático o por sobreuso.\nDolor difuso reumático. NO derrame, zona posterior: '+subt.get())
            etiq_p.grid(column=0, row=0) #posicion
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_sol, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            if subt.get()=='Quiste de Baker' or subt.get()=='Tendinosis poplíteo':
                op = ['ECO']
            else:
                op=['ECO','angio-TC']
            spin_t = ttk.Combobox(v_sol, values=op, state="readonly")
            spin_t.grid(column=1, row=4)   
                 
        # DNI
        etiq_dni = tk.Label(v_sol, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_sol, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_sol, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_ines_aux, e_dni, spin_t, ruta, extra, subt, v_sol, v_t, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_sol,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_sol,text="Atrás", command = v_sol.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_sol.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_sol.grab_set()
        
    def sol_ines_aux(self, dni, tipo, ruta, extra, subt, v_sol, v_t, v_mz, v_d, v_r, v_p, v_rod, v_tipo, v_seg):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([dni.get(),tipo.get()]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
            messagebox.showinfo(title='Paciente no existente', message='El paciente con este número de historial clíncico no existe')

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)
            sos=None
            self.h.seg_rodi(dni.get(),tipo.get(),ruta,extra,subt,sos)
            
            messagebox.showinfo(title='Guardado', message='Diagnóstico guardado') #muestro confirmacion de que el paciente se ha añadido
            messagebox.showinfo(title='En desarrollo', message='Las siguientes secciones de Citación e Informes se desarrollarán en futuras versiones.')            
            try:
                v_sol.destroy()
            except AttributeError:
                pass
            try:
                v_seg.destroy()
            except AttributeError:
                pass
            try:
                v_tipo.destroy()
            except AttributeError:
                pass
            try:
                v_rod.destroy()
            except AttributeError:
                pass
            try:
                v_p.destroy()
            except AttributeError:
                pass
            try:
                v_r.destroy()
            except AttributeError:
                pass
            try:
                v_d.destroy()
            except AttributeError:
                pass
            try:
                v_mz.destroy()
            except AttributeError:
                pass
            try:
                v_t.destroy()
            except AttributeError:
                pass

                
    def rev_seguimiento_onco(self, v_seg):
        #Preparo la finestra
        v_onco = tk.Toplevel(self.v) #creo la finestra
        v_onco.geometry("600x300") #defineixo les seves dimensions
        v_onco.title("Estado de la patología oncológica") #li fico títol
        
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.sol_onco, v_onco, v_seg)
        alta_pac_params2=partial(self.sol_onco2, v_onco, v_seg)
        alta_pac_params3=partial(self.sol_onco3, v_onco, v_seg)
        alta_pac_params4=partial(self.diag_onco, v_onco, v_seg)
      
        # Programar botó    
        etiq_p= tk.Label(v_onco, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_onco, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_onco,text="Control CON tratamiento activo con enfermedad INESTABLE o sospecha de complicación", command = alta_pac_params).grid(column=2,row=6)
        

        etiq_p3= tk.Label(v_onco, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_onco,text="Control CON tratamiento activo con enfermedad ESTABLE", command = alta_pac_params2).grid(column=2,row=10)
        
        etiq_p4= tk.Label(v_onco, text= "    ")
        etiq_p4.grid(column=2, row=8) #posicion
        
        btnAsignar3=tk.Button(v_onco,text="Control SIN tratamiento activo con enfermedad ESTABLE", command = alta_pac_params3).grid(column=2,row=14)
        
        etiq_p5= tk.Label(v_onco, text= "    ")
        etiq_p5.grid(column=2, row=12) #posicion
        
        btnAsignar4=tk.Button(v_onco,text="Proceso de diagnóstico", command = alta_pac_params4).grid(column=2,row=2)
        
        etiq_p5= tk.Label(v_onco, text= "    ")
        etiq_p5.grid(column=2, row=16) #posicion
        
        btnSortir=tk.Button(v_onco,text="Atrás", command = v_onco.destroy).grid(column=2,row=18)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_onco.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_onco.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_onco)
        
    def sol_onco(self, v_onco, v_seg):
        #Preparo la nueva ventana para dar de alta al paciente
        v_so = tk.Toplevel(self.v)
        v_so.geometry("550x350")
        v_so.title("Resumen y guardar") 
        
        etiq_p= tk.Label(v_so, text= "Resumen del diagnóstico:\n    Seguimiento de paciente oncológico con tratamiento activo\ny enfermedad inestable o con sospecha de complicación\n")
        etiq_p.grid(column=0, row=0) #posicion
        
        # Ingreso (desplegable)
        etiq_ing = tk.Label(v_so, text= "Paciente ingresado:")
        etiq_ing.grid(column=0, row=2)
        op = ['Sí','No']
        spin_ing = ttk.Combobox(v_so, values=op, state="readonly")
        spin_ing.grid(column=1, row=2)
        
        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_so, text= "Tipo de prueba de imagen")
        etiq_t.grid(column=0, row=4)
        op = ['RX','ECO','RM','TC']
        spin_t = ttk.Combobox(v_so, values=op, state="readonly")
        spin_t.grid(column=1, row=4)
        
        # DNI
        etiq_dni = tk.Label(v_so, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_so, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_so, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_so, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        ruta = '1'
        alta_pac_params=partial(self.sol_onco_aux, v_dni, spin_ing, spin_t, ruta, v_so, v_onco, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_so,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
        
    def sol_onco_aux(self, dni, ing, tipo, ruta, v_so, v_onco, v_seg):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([dni.get(), ing.get(),tipo.get()]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
            messagebox.showinfo(title='Paciente no existente', message='El paciente con este número de historial clíncico no existe')

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)
            self.h.onco(dni.get(),ing.get(),tipo.get(), ruta)
            
            messagebox.showinfo(title='Guardado', message='Diagnóstico guardado') #muestro confirmacion de que el paciente se ha añadido
            messagebox.showinfo(title='En desarrollo', message='Las siguientes secciones de Citación e Informes se desarrollarán en futuras versiones.')    
            v_so.destroy() #destruyo la ventana
            v_onco.destroy()
            v_seg.destroy()
            
        
    def sol_onco2(self, v_onco, v_seg):
        #Preparo la nueva ventana para dar de alta al paciente
        v_so = tk.Toplevel(self.v)
        v_so.geometry("550x350")
        v_so.title("Resumen y guardar") 
        
        etiq_p= tk.Label(v_so, text= "Resumen del diagnóstico:\n    Seguimiento de paciente oncológico con tratamiento activo\ny enfermedad estable\n")
        etiq_p.grid(column=0, row=0) #posicion
        
        
        # DNI
        etiq_dni = tk.Label(v_so, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=2)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_so, textvariable=v_dni)
        e_dni.grid(column=1, row=2)
        
        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_so, text= "Tipo de prueba de imagen")
        etiq_t.grid(column=0, row=4)
        op = ['RX','ECO','RM','TC']
        spin_t = ttk.Combobox(v_so, values=op, state="readonly")
        spin_t.grid(column=1, row=4)
        
        etiq_p2= tk.Label(v_so, text= "        ")
        etiq_p2.grid(column=0, row=6) #posicion
        
        etiq_p2= tk.Label(v_so, text= "        ")
        etiq_p2.grid(column=1, row=6) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        ruta = '2' 
        ing=None
        alta_pac_params=partial(self.sol_onco2_aux, v_dni, ing, spin_t, ruta, v_so, v_onco, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_so,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=8)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=0,row=8) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
        
    def sol_onco2_aux(self, dni, ing, tipo, ruta, v_so, v_onco, v_seg):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([dni.get(),tipo.get()]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
            messagebox.showinfo(title='Paciente no existente', message='El paciente con este número de historial clíncico no existe')

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)

            self.h.onco(dni.get(),ing,tipo.get(), ruta)
            
            messagebox.showinfo(title='Guardado', message='Diagnóstico guardado') #muestro confirmacion de que el paciente se ha añadido
            messagebox.showinfo(title='En desarrollo', message='Las siguientes secciones de Citación e Informes se desarrollarán en futuras versiones.')    
            v_so.destroy() #destruyo la ventana
            v_onco.destroy()
            v_seg.destroy()
            
            
    def sol_onco3(self, v_onco, v_seg):
        
        #Preparo la nueva ventana para dar de alta al paciente
        v_so = tk.Toplevel(self.v)
        v_so.geometry("550x350")
        v_so.title("Resumen y guardar") 
        
        etiq_p= tk.Label(v_so, text= "Resumen del diagnóstico:\n    Seguimiento de paciente oncológico sin tratamiento activo\ny enfermedad estable\n")
        etiq_p.grid(column=0, row=0) #posicion
        
        # DNI
        etiq_dni = tk.Label(v_so, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=2)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_so, textvariable=v_dni)
        e_dni.grid(column=1, row=2)
        
        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_so, text= "Tipo de prueba de imagen")
        etiq_t.grid(column=0, row=4)
        op = ['RX','ECO','RM','TC']
        spin_t = ttk.Combobox(v_so, values=op, state="readonly")
        spin_t.grid(column=1, row=4)
        
        etiq_p2= tk.Label(v_so, text= "        ")
        etiq_p2.grid(column=0, row=6) #posicion
        
        etiq_p2= tk.Label(v_so, text= "        ")
        etiq_p2.grid(column=1, row=6) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        ruta = '3'
        ing=None
        alta_pac_params=partial(self.sol_onco2_aux, v_dni, ing, spin_t, ruta, v_so, v_onco, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_so,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=8)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=0,row=8) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
        
        
#    def sol_onco3_aux(self, dni, tipo, v_so, v_onco, v_seg):
#        """
#        Auxiliar function to be able to send messageboxes
#        """ 
#        
#        # Mirar si algun esta empty
#        if not all([dni.get(),tipo.get()]):
#            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
#            
#        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
#            messagebox.showinfo(title='Paciente no existente', message='El paciente con este DNI no existe')
#
#        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)
#
#            self.h.onco3(dni.get(),tipo.get())
#            
#            messagebox.showinfo(title='Guardado', message='Dianóstico guardado') #muestro confirmacion de que el paciente se ha añadido
#            v_so.destroy() #destruyo la ventana
#            v_onco.destroy()
#            v_seg.destroy()
    
    def diag_onco(self, v_onco, v_seg):
#        messagebox.showinfo(title='Procedimiento', message='Para seguir en esta sección es imprescindible haber realizado previamnete una RX de 2 proyecciones.\n\nSi no se ha realizado acceder a Revisión > Primera visita > Sospecha de tumor.')    
        
        #Preparo la finestra
        v_diag = tk.Toplevel(self.v) #creo la finestra
        v_diag.geometry("670x300") #defineixo les seves dimensions
        v_diag.title("Zona de la tumoración") #li fico títol
        
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.p_blandas, v_diag, v_onco, v_seg)
        alta_pac_params2=partial(self.hueso_largo, v_diag, v_onco, v_seg)
        alta_pac_params3=partial(self.hueso_plano, v_diag, v_onco, v_seg)        
        
        # Programar botó
        
        etiq_p= tk.Label(v_diag, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_diag, text= "    ")
        etiq_p2.grid(column=1, row=0) #posicion
        etiq_p= tk.Label(v_diag, text= "INFO IMPORTANTE: Para seguir en esta sección es imprescindible haber realizado previamnete una RX de 2 proyecciones.\n\nSi no se ha realizado acceder a Solicitud > Primera visita > Sospecha de tumor.")
        etiq_p.grid(column=1, row=1) #posicion
        
        etiq_p2= tk.Label(v_diag, text= "    ")
        etiq_p2.grid(column=1, row=2) #posicion
        
        btnAsignar=tk.Button(v_diag,text="Partes blandas", command = alta_pac_params).grid(column=1,row=3)
        

        etiq_p3= tk.Label(v_diag, text= "    ")
        etiq_p3.grid(column=1, row=4) #posicion
        
        btnAsignar2=tk.Button(v_diag,text="Hueso largo", command = alta_pac_params2).grid(column=1,row=6)
        
        etiq_p4= tk.Label(v_diag, text= "    ")
        etiq_p4.grid(column=1, row=8) #posicion
        
        btnAsignar3=tk.Button(v_diag,text="Hueso plano", command = alta_pac_params3).grid(column=1,row=14)
        
        
        etiq_p5= tk.Label(v_diag, text= "    ")
        etiq_p5.grid(column=1, row=16) #posicion
        
        btnSortir=tk.Button(v_diag,text="Atrás", command = v_diag.destroy).grid(column=1,row=18)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_diag.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_diag.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_diag)
    
    def p_blandas(self,v_diag,v_onco,v_seg):
            
        ruta='B'
        v_so = tk.Toplevel(self.v)
        v_so.geometry("350x250")
        v_so.title("ECO") 
        
        etiq_p= tk.Label(v_so, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_so, text= "¿Ha realizado ya una ECOGRAFÍA al paciente?")
        etiq_p.grid(column=2, row=2) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rev_eco, ruta, v_so, v_diag, v_onco, v_seg)
        alta_pac_params2=partial(self.sol_rev_post_eco, ruta, v_so, v_diag, v_onco, v_seg)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_so,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_so,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
    
    def sol_rev_eco(self, ruta, v_so, v_diag, v_onco, v_seg):
        v_t=None
        v_m=None
        v_p=None
        v_rm=None
        #Preparo la nueva ventana para dar de alta al paciente
        v_eco = tk.Toplevel(self.v)
        v_eco.geometry("690x350")
        v_eco.title("Resumen y guardar") 
        
        ruta = 'ecoB'
    
        etiq_p= tk.Label(v_eco, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en partes blandas.")
        etiq_p.grid(column=0, row=0) #posicion

        
        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_eco, text= "Tipo de prueba de imagen")
        etiq_t.grid(column=0, row=4)
        op = ['ECO']
        spin_t = ttk.Combobox(v_eco, values=op, state="readonly")
        spin_t.grid(column=1, row=4)
                
        # DNI
        etiq_dni = tk.Label(v_eco, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_eco, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_eco, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_eco, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rm_aux, v_dni, spin_t, ruta, v_rm, v_p, v_m, v_eco, v_t, v_so, v_diag, v_onco, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_eco,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_eco,text="Atrás", command = v_eco.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_eco.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_eco.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_eco)
        
    def sol_rev_post_eco(self, ruta, v_so, v_diag, v_onco, v_seg):
        v_p=None
        v_m=None
        
        v_t = tk.Toplevel(self.v)
        v_t.geometry("350x250")
        v_t.title("Tamaño y morfología") 
        
        etiq_p= tk.Label(v_t, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.mat, ruta, v_t, v_so, v_diag, v_onco, v_seg)
        alta_pac_params2=partial(self.sol_rev_post_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        
         # Programar botó
        btnAsignar=tk.Button(v_t,text="Menor de 5cm, superficial a la fascia y\ncon caracterización fundada y razonable.", command = alta_pac_params2).grid(column=2,row=2)
        #con el boton continuar se manda al metodo alta_pac_aux
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_t,text="Mayor de 5cm, en profundidad a la fascia\no no caracterizable.", command = alta_pac_params).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_t, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_t,text="Atrás", command = v_t.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_t.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_t.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_t)
    
    def mat(self, ruta, v_t, v_so, v_diag, v_onco, v_seg):
          
        v_m = tk.Toplevel(self.v)
        v_m.geometry("350x250")
        v_m.title("Tipo de matriz") 
        
        etiq_p= tk.Label(v_m, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.cara, ruta, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        alta_pac_params2=partial(self.no_cara, ruta, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        
         # Programar botó
        btnAsignar=tk.Button(v_m,text="Matriz no calcificada", command = alta_pac_params2).grid(column=2,row=2)
        #con el boton continuar se manda al metodo alta_pac_aux
        
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_m,text="Matriz calcificada", command = alta_pac_params).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_m, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_m,text="Atrás", command = v_m.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_m.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_m.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_m)
    
    def cara(self, ruta, v_m, v_t, v_so, v_diag, v_onco, v_seg):
        ruta='BC'
        mens="¿Ha realizado ya un TC o RM al paciente?"

        v_p = tk.Toplevel(self.v)
        v_p.geometry("350x250")
        v_p.title("TC/RM") 
        
        etiq_p= tk.Label(v_p, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_p, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_p, text= mens)
        etiq_p.grid(column=2, row=2) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rev_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        alta_pac_params2=partial(self.sol_rev_post_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        
        etiq_p2= tk.Label(v_p, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_p,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_p,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_p, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_p,text="Atrás", command = v_p.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_p.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_p.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_p)
        
    def no_cara(self, ruta, v_m, v_t, v_so, v_diag, v_onco, v_seg):
        ruta='BNC'

        mens="¿Ha realizado ya un TC al paciente?"
            
        v_p = tk.Toplevel(self.v)
        v_p.geometry("350x250")
        v_p.title("TC") 
        
        etiq_p= tk.Label(v_p, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_p, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_p, text= mens)
        etiq_p.grid(column=2, row=2) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rev_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        alta_pac_params2=partial(self.sol_rev_post_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        
        etiq_p2= tk.Label(v_p, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_p,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_p,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_p, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_p,text="Atrás", command = v_p.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_p.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_p.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_p)
        
#        
#    def preg(self, ruta, v_m, v_t, v_so, v_diag, v_onco, v_seg):
#        if ruta=='BC':
#            mens="¿Ha realizado ya un TC o RM al paciente?"
#        if ruta=='BNC':
#            mens="¿Ha realizado ya un TC al paciente?"
#            
#        v_p = tk.Toplevel(self.v)
#        v_p.geometry("350x250")
#        v_p.title("TC") 
#        
#        etiq_p= tk.Label(v_p, text= "    ")
#        etiq_p.grid(column=0, row=0) #posicion
#        etiq_p2= tk.Label(v_p, text= "    ")
#        etiq_p2.grid(column=2, row=0) #posicion
#        
#        etiq_p= tk.Label(v_p, text= mens)
#        etiq_p.grid(column=2, row=2) #posicion
#        
#        # de la llibreria functools
#        # assignar parcial per a funció, per a poder assignar directament command amb variables
#        alta_pac_params=partial(self.sol_rev_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
#        alta_pac_params2=partial(self.sol_rev_post_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
#        
#        etiq_p2= tk.Label(v_p, text= "    ")
#        etiq_p2.grid(column=2, row=4) #posicion
#        
#        # Programar botó
#        btnAsignar=tk.Button(v_p,text="No", command = alta_pac_params).grid(column=3,row=6)
#        #con el boton continuar se manda al metodo alta_pac_aux
#        btnAsignar2=tk.Button(v_p,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
#        
#        etiq_p2= tk.Label(v_p, text= "    ")
#        etiq_p2.grid(column=2, row=8) #posicion
#        
#        #con el boton continuar se manda al metodo alta_pac_aux
#        btnSortir=tk.Button(v_p,text="Atrás", command = v_p.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana
#
#        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
#        v_p.transient()
#
#        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
#        v_p.grab_set()
#
#        # Wait for the window to end
#        self.v.wait_window(v_p)
        
    def hueso_largo(self,v_diag,v_onco,v_seg):
        v_t=None
        v_m=None
        v_p=None
        ruta = 'HL'
        v_so = tk.Toplevel(self.v)
        v_so.geometry("350x250")
        v_so.title("TC") 
        
        etiq_p= tk.Label(v_so, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
         # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rev_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        alta_pac_params2=partial(self.sol_rev_post_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        
         # Programar botó
        btnAsignar=tk.Button(v_so,text="Caracterización fundada y razonable.", command = alta_pac_params2).grid(column=2,row=2)
        #con el boton continuar se manda al metodo alta_pac_aux
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_so,text="No caracterizable", command = alta_pac_params).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
        
    def hueso_plano(self,v_diag,v_onco,v_seg):
        v_t=None
        v_m=None
        v_p=None
        ruta='HP'
        v_so = tk.Toplevel(self.v)
        v_so.geometry("350x250")
        v_so.title("TC") 
        
        etiq_p= tk.Label(v_so, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        
        etiq_p= tk.Label(v_so, text= "¿Ha realizado ya el TC al paciente?")
        etiq_p.grid(column=2, row=2) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rev_tc, ruta,v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        alta_pac_params2=partial(self.sol_rev_post_tc, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=4) #posicion
        
        # Programar botó
        btnAsignar=tk.Button(v_so,text="No", command = alta_pac_params).grid(column=3,row=6)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnAsignar2=tk.Button(v_so,text="Sí", command = alta_pac_params2).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_so, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_so,text="Atrás", command = v_so.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_so.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_so.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_so)
                
    def sol_rev_tc(self, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg):

        #Preparo la nueva ventana para dar de alta al paciente
        v_rm = tk.Toplevel(self.v)
        v_rm.geometry("690x350")
        v_rm.title("Resumen y guardar") 
        v_tc=None
        if ruta == 'HP':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en hueso plano.")
            etiq_p.grid(column=0, row=0) #posicion

            ruta = 'tcHP'

            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_rm, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['TC']
            spin_t = ttk.Combobox(v_rm, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
        
        if ruta == 'HL':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en hueso largo. No caracterizable.")
            etiq_p.grid(column=0, row=0) #posicion
                        
            ruta = 'tcHL'

            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_rm, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['TC']
            spin_t = ttk.Combobox(v_rm, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta == 'BC':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en partes blandas.\nMayor de 5cm en profundidad a la fascia o no caracterizable\nMatriz calcificada.")
            etiq_p.grid(column=0, row=0) #posicion
                        
            ruta = 'tcBC'

            
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_rm, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['TC','RM']
            spin_t = ttk.Combobox(v_rm, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            
        if ruta == 'BNC':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en partes blandas.\nMayor de 5cm en profundidad a la fascia o no caracterizable\nMatriz NO calcificada.")
            etiq_p.grid(column=0, row=0) #posicion
                        
            ruta = 'tcBNC'

            
            # Tipo de prueba de imagen (desplegable)
            etiq_t = tk.Label(v_rm, text= "Tipo de prueba de imagen")
            etiq_t.grid(column=0, row=4)
            op = ['TC']
            spin_t = ttk.Combobox(v_rm, values=op, state="readonly")
            spin_t.grid(column=1, row=4)
            

        # DNI
        etiq_dni = tk.Label(v_rm, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_rm, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_rm, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_rm, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rm_aux, v_dni, spin_t, ruta, v_rm, v_p, v_m, v_tc, v_t, v_so, v_diag, v_onco, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_rm,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_rm,text="Atrás", command = v_rm.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_rm.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_rm.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_rm)
    
    def sol_rev_post_tc(self, ruta, v_p, v_m, v_t, v_so, v_diag, v_onco, v_seg):
        #Preparo la finestra
        v_tc = tk.Toplevel(self.v) #creo la finestra
        v_tc.geometry("500x200") #defineixo les seves dimensions
        v_tc.title("Estado de la patología") #li fico títol
        
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.sol_rm, ruta,v_p, v_m, v_tc, v_t, v_so, v_diag, v_onco, v_seg)
        alta_pac_params2=partial(self.tto, ruta,v_p, v_m, v_tc, v_t, v_so, v_diag, v_onco, v_seg)

        # Programar botó
        
        etiq_p= tk.Label(v_tc, text= "    ")
        etiq_p.grid(column=0, row=0) #posicion
        etiq_p2= tk.Label(v_tc, text= "    ")
        etiq_p2.grid(column=2, row=0) #posicion
        btnAsignar=tk.Button(v_tc,text="Lesión no agresiva y claramente benigna", fg='green', command = alta_pac_params2).grid(column=2,row=2)
        

        etiq_p3= tk.Label(v_tc, text= "    ")
        etiq_p3.grid(column=2, row=4) #posicion
        
        btnAsignar2=tk.Button(v_tc,text="Lesión agresiva con sospecha de malignidad o dudas", fg='red', command = alta_pac_params).grid(column=2,row=6)
        
        etiq_p2= tk.Label(v_tc, text= "    ")
        etiq_p2.grid(column=2, row=8) #posicion
        
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_tc,text="Atrás", command = v_tc.destroy).grid(column=2,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_tc.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_tc.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_tc)
        
        
    def sol_rm(self, ruta, v_p, v_m, v_tc, v_t, v_so, v_diag, v_onco, v_seg):
        #Preparo la nueva ventana para dar de alta al paciente
        v_rm = tk.Toplevel(self.v)
        v_rm.geometry("690x350")
        v_rm.title("Resumen y guardar") 
        
        if ruta == 'HP':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en hueso plano. Lesión agresiva con sospecha de malignidad o dudas.")
            etiq_p.grid(column=0, row=0) #posicion

            ruta = 'HPR'
            
        if ruta == 'HL':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en hueso largo con caracterización fundada y razonable.\nLesión agresiva con sospecha de malignidad o dudas.")
            etiq_p.grid(column=0, row=0) #posicion

            ruta = 'HLR'  
        if ruta == 'B':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en partes blandas\nMenor de 5cm, superficial a la fascia y con caracterización fundada y razonable.\nLesión agresiva con sospecha de malignidad o dudas.")
            etiq_p.grid(column=0, row=0) #posicion

            ruta = 'BR'  
            
        if ruta == 'BC':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en partes blandas\nMayor de 5cm en profundidad a la fascia o no caracterizable\nMatriz calcificada.\nLesión agresiva con sospecha de malignidad o dudas.")
            etiq_p.grid(column=0, row=0) #posicion

            ruta = 'BCR'  
        
        if ruta == 'BNC':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en partes blandas\nMayor de 5cm en profundidad a la fascia o no caracterizable\nMatriz NO calcificada.\nLesión agresiva con sospecha de malignidad o dudas.")
            etiq_p.grid(column=0, row=0) #posicion

            ruta = 'BNCR' 
                    
        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_rm, text= "Tipo de prueba de imagen")
        etiq_t.grid(column=0, row=4)
        op = ['RM + Derivación a COMTE de sarcomas de referencia']
        spin_t = ttk.Combobox(v_rm, values=op, state="readonly")
        spin_t.grid(column=1, row=4)     
        
        # DNI
        etiq_dni = tk.Label(v_rm, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_rm, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_rm, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_rm, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rm_aux, v_dni, spin_t, ruta, v_rm, v_p, v_m, v_tc, v_t, v_so, v_diag, v_onco, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_rm,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_rm,text="Atrás", command = v_rm.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_rm.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_rm.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_rm)
        
    def sol_rm_aux(self, dni, tipo, ruta, v_rm, v_p, v_m, v_tc, v_t, v_so, v_diag, v_onco, v_seg):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        
        # Mirar si algun esta empty
        if not all([dni.get(),tipo.get()]):
            messagebox.showerror(title='Error', message='Alguno de los campos está vacío') #mensaje de error
            
        elif self.h.comprueba_nomalta(dni.get(),'P') == False: #si el paciente no existe
            messagebox.showinfo(title='Paciente no existente', message='El paciente con este número de historial clíncico no existe')

        else: #si todos los datos introducidos son correctos (pasan los filtros que hemos puesto)
            ing=None
            self.h.onco(dni.get(),ing,tipo.get(),ruta)
            
            messagebox.showinfo(title='Guardado', message='Diagnóstico guardado') #muestro confirmacion de que el paciente se ha añadido
            messagebox.showinfo(title='En desarrollo', message='Las siguientes secciones de Citación e Informes se desarrollarán en futuras versiones.')                
#            if ruta != 'ecoB':
            print('hola')
            try:
                v_rm.destroy() #destruyo la ventana
            except AttributeError:
                pass
            try:
                v_tc.destroy()
            except AttributeError:
                pass
            try:
                v_t.destroy()
            except AttributeError:
                pass
            try:
                v_p.destroy()
                print('p')
            except AttributeError:
                pass
            try:
                v_m.destroy()
                print('m')
            except AttributeError:
                pass

#            if ruta != 'tcHP' and ruta!= 'tcHL' and ruta!='tcBC' and ruta!='tcBNC':
#                v_tc.destroy()
#            if ruta=='BR' or ruta=='BT':
#                v_t.destroy()
#            if ruta == 'BCR' or ruta== 'BCT' or ruta=='BNCR' or ruta=='BNCT':
#                v_p.destroy()
#                v_m.destroy()
#                v_t.destroy()
#                
            v_so.destroy()
            v_diag.destroy()
            v_onco.destroy()
            v_seg.destroy()
            
            
    def tto(self, ruta, v_p, v_m, v_tc, v_t, v_so, v_diag, v_onco, v_seg):
        #Preparo la nueva ventana para dar de alta al paciente
        v_rm = tk.Toplevel(self.v)
        v_rm.geometry("650x350")
        v_rm.title("Resumen y guardar") 
        
        if ruta == 'HP':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en hueso plano. Lesión no agresiva y claramente benigna.")
            etiq_p.grid(column=0, row=0) #posicion
            
            ruta = 'HPT'
        if ruta == 'HL':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en hueso largo con caracterización fundada y razonable.\nLesión no agresiva y claramente benigna.")
            etiq_p.grid(column=0, row=0) #posicion
            
            ruta = 'HLT'
        if ruta == 'B':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en partes blandas.\nMenor de 5cm, superficial a la fascia y\ncon caracterización fundada y razonable.\nLesión no agresiva y claramente benigna.")
            etiq_p.grid(column=0, row=0) #posicion
            
            ruta = 'BT'
            
        if ruta == 'BC':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en partes blandas.\nMayor de 5cm en profundidad a la fascia o no caracterizable\nMatriz calcificable. Lesión no agresiva y claramente benigna.")
            etiq_p.grid(column=0, row=0) #posicion
            
            ruta = 'BCT'
            
        if ruta == 'BNC':
            etiq_p= tk.Label(v_rm, text= "Resumen del diagnóstico:\n    Seguimiento de tumor en partes blandas.\nMayor de 5cm en profundidad a la fascia o no caracterizable\nMatriz NO calcificable. Lesión no agresiva y claramente benigna.")
            etiq_p.grid(column=0, row=0) #posicion
            
            ruta = 'BNCT'
            
        # Tipo de prueba de imagen (desplegable)
        etiq_t = tk.Label(v_rm, text= "Tipo de prueba de imagen")
        etiq_t.grid(column=0, row=4)
        op = ['No hay pruebas indicadas. Tratamiento / vigilancia / fin del estudio.']
        spin_t = ttk.Combobox(v_rm, values=op, state="readonly")
        spin_t.grid(column=1, row=4)   
        
        # DNI
        etiq_dni = tk.Label(v_rm, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=6)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_rm, textvariable=v_dni)
        e_dni.grid(column=1, row=6)
        
        etiq_p2= tk.Label(v_rm, text= "        ")
        etiq_p2.grid(column=0, row=8) #posicion
        
        etiq_p2= tk.Label(v_rm, text= "        ")
        etiq_p2.grid(column=1, row=8) #posicion
        
        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        alta_pac_params=partial(self.sol_rm_aux, v_dni, spin_t, ruta, v_rm, v_p, v_m, v_tc, v_t, v_so, v_diag, v_onco, v_seg)

        # Programar botó
        btnAsignar=tk.Button(v_rm,text="Guardar diagnóstico", command = alta_pac_params).grid(column=1,row=10)
        #con el boton continuar se manda al metodo alta_pac_aux
        btnSortir=tk.Button(v_rm,text="Atrás", command = v_rm.destroy).grid(column=0,row=10) #boton salir: se cierra la ventana

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_rm.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_rm.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_rm)
            
        
        
    """################################################################################
    ################################################################################
    ################################ BUSCAR #########################################
    ################################################################################ 
    ################################################################################"""
    
    def consulta_paciente(self):
        """
        Funció que implementa una finestra amb la consulta de pacient.
        """
        #Preparo la finestra
        v_consulta = tk.Toplevel(self.v) #creo la finestra
        v_consulta.geometry("395x200") #defineixo les seves dimensions
        v_consulta.title("Búsqueda paciente") #li fico títol
    
        # Label amb la info del que s'ha dintorudir per pantalla
        etiq_0= tk.Label(v_consulta, text= "Insertar número de historial clínico del paciente \n que desea buscar:")
        etiq_0.grid(column=0, row=0)

        # l'adquisició de variables amb entries ja ha estat explicada a altas per tant no ho tornarem a exlpicar al llarg del codi
        
        # Nom
        etiq_dni = tk.Label(v_consulta, text= "Número de historial clínico:")
        etiq_dni.grid(column=0, row=1)
        v_dni = tk.StringVar()
        v_dni.set("")
        e_dni = tk.Entry(v_consulta, textvariable=v_dni)
        e_dni.grid(column=1, row=1)

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.consulta_pac_aux, v_dni, v_consulta)

        # Programar botó
        btnAsignar=tk.Button(v_consulta,text="Consultar", command = alta_pac_params).grid(column=1,row=8)
        btnSortir=tk.Button(v_consulta,text="Salir", command = v_consulta.destroy).grid(column=0,row=8)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_consulta.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_consulta.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_consulta)

    def consulta_pac_aux(self, dni, v_consulta):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        # Mirar si esta empty
        if not dni.get():
            messagebox.showerror(title='Error', message='No se ha introducido ningún nombre.')
        else:
            mensaje=self.h.consult_pac(dni.get())
            messagebox.showinfo(title='Paciente', message=mensaje)
            
            
    def consulta_paciente_nom(self):
        """
        Funció que implementa una finestra amb la consulta de pacient.
        """
        #Preparo la finestra
        v_consulta = tk.Toplevel(self.v) #creo la finestra
        v_consulta.geometry("375x200") #defineixo les seves dimensions
        v_consulta.title("Búsqueda paciente") #li fico títol
    
        # Label amb la info del que s'ha dintorudir per pantalla
        etiq_0= tk.Label(v_consulta, text= "Insertar nombre del paciente \n que desea buscar:")
        etiq_0.grid(column=0, row=0)

        # l'adquisició de variables amb entries ja ha estat explicada a altas per tant no ho tornarem a exlpicar al llarg del codi
        
        # Nom
        etiq_nom = tk.Label(v_consulta, text= "Nombre:")
        etiq_nom.grid(column=0, row=1)
        v_nom = tk.StringVar()
        v_nom.set("")
        e_nom = tk.Entry(v_consulta, textvariable=v_nom)
        e_nom.grid(column=1, row=1)

        # de la llibreria functools
        # assignar parcial per a funció, per a poder assignar directament command amb variables
        #accedim al métode auxiliar
        alta_pac_params=partial(self.consulta_pac_nom_aux, v_nom, v_consulta)

        # Programar botó
        btnAsignar=tk.Button(v_consulta,text="Consultar", command = alta_pac_params).grid(column=1,row=8)
        btnSortir=tk.Button(v_consulta,text="Salir", command = v_consulta.destroy).grid(column=0,row=8)

        # Funcio per a obligar aquesta finestra a estar damunt de la anterior (estètic)
        v_consulta.transient()

        #Funcio per a obligar aquesta finestra a tenir l'atenció, i fa que no es puguin fer inputs a l'anterior
        v_consulta.grab_set()

        # Wait for the window to end
        self.v.wait_window(v_consulta)

    def consulta_pac_nom_aux(self, nom, v_consulta):
        """
        Auxiliar function to be able to send messageboxes
        """ 
        # Mirar si esta empty
        if not nom.get():
            messagebox.showerror(title='Error', message='No se ha introducido ningún nombre')
        else:
            # crido al métode consulta paciente de l'hospital que em retornará una llista amb la info del pacient
            result = self.h.consult_pac_nom(nom.get().title())
            if result== '': #si la llista està buida vol dir que no s'ha trobat cap pacient amb aquest nom
                messagebox.showerror(title='Error', message='Paciente no encontrado')
            else:
                men='Paciente/s con los datos introducidos:\n\n'
                men+=result
                messagebox.showinfo(title='Paciente/s', message=men)
                
                
        """################################################################################
    ################################################################################
    ################################ EXPORTAR #########################################
    ################################################################################ 
    ################################################################################"""
    
    def archivo(self):
        self.h.gen_arch()
        messagebox.showinfo(title='Guardado', message='Archivo guardado correctamente')
    