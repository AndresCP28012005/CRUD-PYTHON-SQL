from tkinter import *
from conexion import *
from codeLabel import *

# Este elemento nos permite que el Entry de ID solo acepte numeros (declarado en la linea de codigo 74)
validate_entry = lambda text: text.isdecimal()
# --------------------------------------------
raiz = Tk()

raiz.iconbitmap('.\logo.ico')

# Estas variables son declaradas de esta manera para poder devolver datos de SQL a los Entrys
miId=StringVar()
miNombre = StringVar()
miApellido=StringVar()
miPassword=StringVar()
miDireccion=StringVar()
miComentario=StringVar()
# ---------------------



barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)

archivoBbdd=Menu(barraMenu, tearoff=0)
archivoBbdd.add_command(label='Conectar', command=MenuOpciones.conectar)
archivoBbdd.add_command(label='Salir', command=MenuOpciones.salirAplicacion)



archivoBorrar=Menu(barraMenu, tearoff=0)
archivoBorrar.add_command(label='Limpiar campos', command=MenuOpciones.clear)

archivoCRUD=Menu(barraMenu, tearoff=0)
archivoCRUD.add_command(label='Create', command=lambda:llamarCrud(1))
archivoCRUD.add_command(label='Read', command=lambda:llamarCrud(2))
archivoCRUD.add_command(label='Update', command=lambda:llamarCrud(3))
archivoCRUD.add_command(label='Delete', command=lambda:llamarCrud(4))

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label='Contacto', command=lambda:MenuOpciones.ayuda(1))
archivoAyuda.add_command(label='Autor', command=lambda:MenuOpciones.ayuda(2))

barraMenu.add_cascade(label='BBDD', menu=archivoBbdd)
barraMenu.add_cascade(label='Borrar', menu=archivoBorrar)
barraMenu.add_cascade(label='CRUD', menu=archivoCRUD)
barraMenu.add_cascade(label='Ayuda', menu=archivoAyuda)



# ----------------------LABEL------------------


miFrame=Frame(raiz, width=600, height=400)
miFrame.pack()

idLabel=Label(miFrame, text='id*:')
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text='Nombre*:')
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text='Apellido*:')
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passwordLabel=Label(miFrame, text='Password*:')
passwordLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text='Direccion*:')
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text='Comentario:')
comentarioLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# ---------------CUADROS----------------

cuadroId = Entry(miFrame, textvariable=miId, validate="key", validatecommand=(raiz.register(validate_entry),"%S"))
cuadroId.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroApellido = Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPassword = Entry(miFrame, textvariable=miPassword)
cuadroPassword.grid(row=3, column=1, padx=10, pady=10)
cuadroPassword.config(show='*')

cuadroDireccion = Entry(miFrame, textvariable=miDireccion)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

cuadroComentario = Text(miFrame, width=16, height=5)
cuadroComentario.grid(row=5, column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=cuadroComentario.yview)
scrollVert.grid(row=5, column=2, sticky='nsew')
cuadroComentario.config(yscrollcommand=scrollVert.set)

# ------------------------BOTONES-------------------------

contenedorBotones=Frame(raiz)
contenedorBotones.pack()

botonCreate=Button(contenedorBotones, text='Create', command=lambda:llamarCrud(1))
botonCreate.grid(row=6, column=0, padx=10, pady=10)


botonRead=Button(contenedorBotones, text='Read', command=lambda:llamarCrud(2))
botonRead.grid(row=6, column=1, padx=10, pady=10)


botonUpdate=Button(contenedorBotones, text='Update', command=lambda:llamarCrud(3))
botonUpdate.grid(row=6, column=2, padx=10, pady=10)


botonDelete=Button(contenedorBotones, text='Delete', command=lambda:llamarCrud(4))
botonDelete.grid(row=6, column=3, padx=10, pady=10)




raiz.mainloop()