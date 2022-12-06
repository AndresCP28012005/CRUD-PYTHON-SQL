import sqlite3
import interfaz
from tkinter import messagebox

# ----------------CODE LABEL HACE REFERENCIA AL CODIGO DETRÁS DE LO QUE SE VE EN LOS LABEL DE "BBDD", "BORRAR", "CRUD" Y "AYUDA", MÁS SIN EMBARGO LO INVOLUCRADO EN LA INTERFAZ GRAFICA ESTA EN EL ARHCIVO interfaz.py-----

class MenuOpciones:
    # -------------------------LABEL CONECTAR-----------------------
    
    def conectar():
        # ------------HACEMOS EL PROCESO DE CONEXION DE SQL----------   
        
        miConexion=sqlite3.connect('ConectoresCRUD')
        miCursor=miConexion.cursor()
        
        miCursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="datosUsuarios" ')
        validador=miCursor.fetchmany()
        validador=(len(validador))
            
        if validador==1: 
            messagebox.showinfo('¡Conexion exitosa!','La tabla ya se encuentra creada')
        else:
            validador=0
            
            sql='''
            CREATE TABLE IF NOT EXISTS datosUsuarios (
                id INTEGER IDENTITY(1,1) PRIMARY KEY,
                nombre VARCHAR(50),
                apellido VARCHAR(50),
                password VARCHAR(50),
                direccion VARCHAR(50),
                comentario VARCHAR(50)
                
            )
            '''
            miCursor.execute(sql) 
            
            while validador==0:
                miCursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="datosUsuarios" ')
                validador=len((miCursor.fetchone()))
            messagebox.showinfo('¡Tabla Creada!','La tabla se ha creado')
            

    def salirAplicacion():
        # ---CON ESTA FUNCIION SALIMOS DE LA APLICACION---
        opcion= messagebox.askquestion('Salir','¿Deseas salir de la aplicacion?')
        if opcion=='yes':
            interfaz.raiz.destroy()
            
    def ayuda(self):
        if self==1:
            return messagebox.showinfo('Contacto','Si existe alguna duda puedes contactarme por Linkedin:\nhttps://www.linkedin.com/in/emmanuel-canto-737b55191/')
        else:
            return messagebox.showinfo('Codigo libre','Creado por Emmanuel Canto')

    # -------------------------LABEL BORRAR-----------------------
    def clear():
        #---CON ESTA FUNCION LIMPIAMOS EL CONTENIDO DE LOS ENTRY---
        interfaz.cuadroId.delete('0','end')
        interfaz.cuadroNombre.delete('0', 'end')
        interfaz.cuadroApellido.delete('0', 'end')
        interfaz.cuadroPassword.delete('0', 'end')
        interfaz.cuadroDireccion.delete('0', 'end')
        interfaz.cuadroComentario.delete('1.0', 'end')