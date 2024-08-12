import sqlite3
from tkinter import messagebox
import tkinter as tk

class crud:
    def __init__(self, Id, nombre, apellido, password, direccion, comentario):
        self.id = Id
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.direccion = direccion
        self.comentario = comentario
        self.miConexion = sqlite3.connect('ConectoresCRUD')
        self.miCursor = self.miConexion.cursor()

    def __del__(self):
        self.miConexion.close()

    def ValidarCamposObligatorios(self):
        return all([self.id, self.nombre, self.apellido, self.password, self.direccion])

    def create(self):
        try:
            self.miCursor.execute("INSERT INTO datosUsuarios VALUES(?,?,?,?,?,?)", 
                                  (self.id, self.nombre, self.apellido, self.password, self.direccion, self.comentario))
            self.miConexion.commit()
            return messagebox.showinfo('Usuario Creado', 'El usuario ha sido creado')
        except sqlite3.Error:
            return messagebox.showerror('Error', 'El usuario ya existe o hubo un error en la creación')

    def read(self):
        try:
            self.miCursor.execute('SELECT * FROM datosUsuarios WHERE id=? OR nombre=? OR apellido=?', (self.id, self.nombre, self.apellido))
            query = self.miCursor.fetchone()
            return query
        except:
            return None

    def update(self):
        try:
            self.miCursor.execute('SELECT * FROM datosUsuarios WHERE id=?', (self.id,))
            query = self.miCursor.fetchone()
            datosRecibidos = (self.id, self.nombre, self.apellido, self.password, self.direccion, self.comentario)
            interseccion = [datosRecibidos[q] if datosRecibidos[q] else query[q] for q in range(len(query))]
            self.miCursor.execute('UPDATE datosUsuarios SET nombre=?, apellido=?, password=?, direccion=?, comentario=? WHERE id=?', 
                                  (interseccion[1], interseccion[2], interseccion[3], interseccion[4], interseccion[5], interseccion[0]))
            self.miConexion.commit()
            return messagebox.showinfo('Actualizado','El usuario ha sido actualizado')
        except:
            return messagebox.showinfo('Error','Ocurrió un error. Compruebe que los datos estén llenados correctamente')

    def delete(self):
        self.miCursor.execute('SELECT * FROM datosUsuarios WHERE id=?', (self.id,))
        query = self.miCursor.fetchone()
        if query:
            c = f'¿Desea eliminar el usuario {query[1]} {query[2]}?'
            respuesta = messagebox.askquestion('Confirmar', c)
            if respuesta == 'yes':
                self.miCursor.execute('DELETE FROM datosUsuarios WHERE ID= ?', (self.id,))
                self.miConexion.commit()
                return True
        return False

def llamarCrud(opcion, root):
    miId = root.children['!frame'].children['!entry']
    miNombre = root.children['!frame'].children['!entry2']
    miApellido = root.children['!frame'].children['!entry3']
    miPassword = root.children['!frame'].children['!entry4']
    miDireccion = root.children['!frame'].children['!entry5']
    miComentario = root.children['!frame'].children['!text']

    usuario = crud(miId.get(), miNombre.get(), miApellido.get(), 
                   miPassword.get(), miDireccion.get(), miComentario.get('1.0','end'))

    if opcion == 1:
        if usuario.ValidarCamposObligatorios():
            usuario.create()
        else:
            messagebox.showerror('Error','Verifique que los campos obligatorios estén llenos')
    elif opcion == 2:
        result = usuario.read()
        if result:
            miId.delete(0, tk.END)
            miId.insert(0, result[0])
            miNombre.delete(0, tk.END)
            miNombre.insert(0, result[1])
            miApellido.delete(0, tk.END)
            miApellido.insert(0, result[2])
            miPassword.delete(0, tk.END)
            miPassword.insert(0, result[3])
            miDireccion.delete(0, tk.END)
            miDireccion.insert(0, result[4])
            miComentario.delete('1.0', tk.END)
            miComentario.insert(tk.END, result[5])
        else:
            messagebox.showerror('Error', 'Usuario no encontrado')
    elif opcion == 3:
        usuario.update()
    elif opcion == 4:
        if usuario.delete():
            messagebox.showinfo('Eliminado', 'El usuario ha sido eliminado')
        else:
            messagebox.showerror('Error', 'No se pudo eliminar el usuario')
    else:
        messagebox.showerror('Error', 'Ocurrió un Error')
