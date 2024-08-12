from tkinter import *
from tkinter import messagebox
from crud_functions import llamarCrud
from codeLabel import MenuOpciones

validate_entry = lambda text: text.isdecimal()

raiz = Tk()
raiz.iconbitmap(r'.\logo.ico')

miId, miNombre, miApellido, miPassword, miDireccion, miComentario = [StringVar() for _ in range(6)]

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)

archivoBbdd = Menu(barraMenu, tearoff=0)
archivoBbdd.add_command(label='Conectar', command=MenuOpciones.conectar)
archivoBbdd.add_command(label='Salir', command=lambda: MenuOpciones.salirAplicacion(raiz))

archivoBorrar = Menu(barraMenu, tearoff=0)
archivoBorrar.add_command(label='Limpiar campos', command=lambda: MenuOpciones.clear(widgets_to_clear, cuadroComentario))

archivoCRUD = Menu(barraMenu, tearoff=0)
for label, command in [('Create', 1), ('Read', 2), ('Update', 3), ('Delete', 4)]:
    archivoCRUD.add_command(label=label, command=lambda x=command: llamarCrud(x, raiz))

archivoAyuda = Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label='Contacto', command=lambda: MenuOpciones.ayuda(1))
archivoAyuda.add_command(label='Autor', command=lambda: MenuOpciones.ayuda(2))

for label, menu in [('BBDD', archivoBbdd), ('Borrar', archivoBorrar), ('CRUD', archivoCRUD), ('Ayuda', archivoAyuda)]:
    barraMenu.add_cascade(label=label, menu=menu)

miFrame = Frame(raiz, width=600, height=400)
miFrame.pack()

labels = ['id*:', 'Nombre*:', 'Apellido*:', 'Password*:', 'Direccion*:', 'Comentario:']
entries = [miId, miNombre, miApellido, miPassword, miDireccion]

for i, (label_text, entry_var) in enumerate(zip(labels, entries)):
    Label(miFrame, text=label_text).grid(row=i, column=0, sticky="e", padx=10, pady=10)
    entry = Entry(miFrame, textvariable=entry_var)
    entry.grid(row=i, column=1, padx=10, pady=10)
    if i == 0:
        entry.config(validate="key", validatecommand=(raiz.register(validate_entry),"%S"))
    elif i == 3:
        entry.config(show='*')

cuadroComentario = Text(miFrame, width=16, height=5)
cuadroComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=cuadroComentario.yview)
scrollVert.grid(row=5, column=2, sticky='nsew')
cuadroComentario.config(yscrollcommand=scrollVert.set)

contenedorBotones = Frame(raiz)
contenedorBotones.pack()

widgets_to_clear = [miId, miNombre, miApellido, miPassword, miDireccion]

for i, (text, command) in enumerate([('Create', 1), ('Read', 2), ('Update', 3), ('Delete', 4)]):
    Button(contenedorBotones, text=text, command=lambda x=command: llamarCrud(x, raiz)).grid(row=6, column=i, padx=10, pady=10)

if __name__ == "__main__":
    raiz.mainloop()
