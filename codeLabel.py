import sqlite3
from tkinter import messagebox

class MenuOpciones:
    @staticmethod
    def conectar():
        with sqlite3.connect('ConectoresCRUD') as miConexion:
            miCursor = miConexion.cursor()
            miCursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="datosUsuarios"')
            if not miCursor.fetchone():
                sql = '''
                CREATE TABLE IF NOT EXISTS datosUsuarios (
                    id INTEGER PRIMARY KEY,
                    nombre VARCHAR(50),
                    apellido VARCHAR(50),
                    password VARCHAR(50),
                    direccion VARCHAR(50),
                    comentario VARCHAR(50)
                )
                '''
                miCursor.execute(sql)
                messagebox.showinfo('¡Tabla Creada!','La tabla se ha creado')
            else:
                messagebox.showinfo('¡Conexión exitosa!','La tabla ya se encuentra creada')

    @staticmethod
    def salirAplicacion(raiz):
        if messagebox.askquestion('Salir','¿Deseas salir de la aplicación?') == 'yes':
            raiz.destroy()

    @staticmethod
    def ayuda(opcion):
        if opcion == 1:
            return messagebox.showinfo('Contacto','Si existe alguna duda puedes contactarme por Linkedin:\nhttps://www.linkedin.com/in/emmanuel-canto-737b55191/')
        else:
            return messagebox.showinfo('Código libre','Creado por Emmanuel Canto')

    @staticmethod
    def clear(widgets, text_widget):
        for widget in widgets:
            widget.set('')
        text_widget.delete('1.0', 'end')
