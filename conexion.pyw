import sqlite3
import interfaz
import codeLabel
from tkinter import messagebox
import tkinter as tk
    

class crud:
    miConexion=sqlite3.connect('ConectoresCRUD')
    miCursor=miConexion.cursor()
    
    def __init__(self, Id, nombre, apellido, password, direccion, comentario):
        self.id = Id
        self.nombre = nombre
        self.apellido = apellido
        self.password =  password
        self.direccion = direccion
        self.comentario = comentario

    def ValidarCamposObligatorios(self):
    # -----LA VALIDACION DE LOS DATOS ES IMPORTANTE, AQUI VALIDAMOS QUE LOS DATOS OBLIGATORIOS PARA CREAR USUARIOS NUEVOS. Y SÍ SE NECESITA PARA ALGUN COMPORTAMIENTO A FUTURO YA ESTA PREPARADO PARA USAR.
        if self.id and self.nombre and self.apellido and self.password and self.direccion:
            print('Todos los campos obligatorios han sido llenado')   
            return True
        else:
            return          

    
    def create(self):
    #----- METODO PARA CREAR LOS USUARIOS-----
                try:
                    crud.miCursor.execute("INSERT INTO datosUsuarios VALUES(?,?,?,?,?,?)", (self.id, self.nombre,self.apellido, self.password,self.direccion, self.comentario))
                    crud.miConexion.commit()
                    return messagebox.showinfo('Usuario Creado', 'El usuario ha sido creado')
                except ValueError:
                    return messagebox.showerror('Campos incorrectos', 'Revise que los datos hayan sido ingresados de manera correcta')
                except sqlite3.Error:
                    return messagebox.showerror('Usuario creado', 'El usuario ya ha sido crado.')
                
    def read(self):
    # -----METODO PARA LEER DATOS----
        try:
            crud.miCursor.execute('SELECT * FROM datosUsuarios WHERE id=? OR nombre=? OR apellido=?', (self.id, self.nombre, self.apellido))
            query=crud.miCursor.fetchone()
            codeLabel.MenuOpciones.clear()
            return interfaz.miId.set(query[0]), interfaz.miNombre.set(query[1]), interfaz.miApellido.set(query[2]), interfaz.miPassword.set(query[3]), interfaz.miDireccion.set(query[4]), interfaz.cuadroComentario.insert(tk.INSERT, query[5])
        except:
            return messagebox.showerror('Error', 'Usuario no encontrado')
            
    def update(self):
    # -----METODO PAR ACTUALIZAR DATOS-----
        try:
            crud.miCursor.execute('SELECT * FROM datosUsuarios WHERE id=?', (self.id))
            query=crud.miCursor.fetchone()
            datosRecibidos=(self.id, self.nombre,self.apellido, self.password,self.direccion, self.comentario)
            
            interseccion=[] #esta variable sirve para unir lo nuevo de la tupla "datosRecibidos" con lo de la query generando una lista con los nuevos datos y conservando lo anterior en caso de que no se llene

            for q in range(len(query)):
                if datosRecibidos[q]=="":
                    interseccion.append(query[q])
                else:
                    interseccion.append(datosRecibidos[q])
                    
            interseccion=tuple(interseccion)

            crud.miCursor.execute('UPDATE datosUsuarios SET nombre=?, apellido=?, password=?, direccion=?, comentario=? WHERE id=?', (interseccion[1], interseccion[2], interseccion[3], interseccion[4], interseccion[5], interseccion[0]))
            return messagebox.showinfo('Actualizado','El usuario ha sido actualizado')
        except:
            return messagebox.showinfo('Error','Ocurrio un error compruebe que los datos esten llenados correctamente')
    def delete(self):
    # -----METOD PARA ELIMINAR USUARIO-----
            crud.miCursor.execute('SELECT * FROM datosUsuarios WHERE id=?', (self.id))
            query=crud.miCursor.fetchone()
            
            a='¿Desea eliminar el usuario '
            b='?'
            c= a + query[1] + " " +query[2] + b
            
            respuesta = messagebox.askquestion('Confirmar',c)
            if respuesta=='yes':
                crud.miCursor.execute('DELETE FROM datosUsuarios WHERE ID= ?', self.id )
        

def llamarCrud(opcion):
    usuario=crud(interfaz.cuadroId.get(), interfaz.cuadroNombre.get() ,interfaz.cuadroApellido.get(), interfaz.cuadroPassword.get(), interfaz.cuadroDireccion.get(), interfaz.cuadroComentario.get('1.0','end'))

    if opcion==1:
        validacion=crud.ValidarCamposObligatorios(usuario)
        if validacion==True:
            usuario.create()
        else:
            return messagebox.showerror('Error','Verifique que los campos sean llenados correctamente')
    elif opcion==2:
        usuario.read()
    elif opcion==3:
        usuario.update()
    elif opcion==4:
        usuario.delete()
    else:
        messagebox.showerror('Error', 'Ocurrio un Error')
