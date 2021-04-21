
from tkinter import *


raiz=Tk()#Creacion de la Raiz

miFrame=Frame(raiz) #Creacion del Framew

miFrame.pack()#Empaquetado del Frame

#---------------------------------------------Pantalla------------------------------------------



numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)# Creacion del cuadro de texto de las operaciones
pantalla.grid(row=1,column=1, padx=10, pady=10, columnspan=4)#Cubicacion del cadro de texto dentro de la cuadricula, la cuadricula ya esta creada unicamente se ban agregando elementos a la misma
pantalla.config(background='Black', fg='#03f943', justify='right')
pantalla.insert(0,'0')


#---------------------------Pulsaciones del teclado -----------------------------------


def numeroPulsado(num):
    if numeroPantalla.get() == '0':
        numeroPantalla.set(num)
    else:
        numeroPantalla.set(numeroPantalla.get() + num)
        #numeroPantalla.set(num)



#---------------------------Funciones de la calculadora --------------------------------------

listHistoricoTransacciones = []

def suma():
    listHistoricoTransacciones.append(numeroPantalla.get())
    print(listHistoricoTransacciones)





#---------------------------Creación de los Botones Fila 1------------------------------------------

                                 #Ancho del Boton =3             
Boton7=Button(miFrame, text='7', width=3, command=lambda:numeroPulsado('7'))
Boton7.grid(row=2, column=1)
Boton8=Button(miFrame, text='8', width=3, command=lambda:numeroPulsado('8'))
Boton8.grid(row=2, column=2)
Boton9=Button(miFrame, text='9', width=3, command=lambda:numeroPulsado('9'))
Boton9.grid(row=2, column=3)
BotonDividir=Button(miFrame, text='/', width=3,)
BotonDividir.grid(row=2, column=4)


#---------------------------Creación de los Botones Fila 2------------------------------------------

                                 #Ancho del Boton =3             
Boton4=Button(miFrame, text='4', width=3, command=lambda:numeroPulsado('4'))
Boton4.grid(row=3, column=1)
Boton5=Button(miFrame, text='5', width=3, command=lambda:numeroPulsado('5'))
Boton5.grid(row=3, column=2)
Boton6=Button(miFrame, text='6', width=3, command=lambda:numeroPulsado('6'))
Boton6.grid(row=3, column=3)
BotonDividir=Button(miFrame, text='*', width=3)
BotonDividir.grid(row=3, column=4)

#---------------------------Creación de los Botones Fila 3------------------------------------------

                                 #Ancho del Boton =3             
Boton1=Button(miFrame, text='1', width=3, command=lambda:numeroPulsado('1'))
Boton1.grid(row=4, column=1)
Boton2=Button(miFrame, text='2', width=3, command=lambda:numeroPulsado('2'))
Boton2.grid(row=4, column=2)
Boton3=Button(miFrame, text='3', width=3, command=lambda:numeroPulsado('3'))
Boton3.grid(row=4, column=3)
BotonRestar=Button(miFrame, text='-', width=3)
BotonRestar.grid(row=4, column=4)

#---------------------------Creación de los Botones Fila 4------------------------------------------

                                 #Ancho del Boton =3             
Boton0=Button(miFrame, text='0', width=3, command=lambda:numeroPulsado('0'))
Boton0.grid(row=5, column=1)
BotonComa=Button(miFrame, text=',', width=3)
BotonComa.grid(row=5, column=2)
BotonIgual=Button(miFrame, text='=', width=3)
BotonIgual.grid(row=5, column=3)
BotonSumar=Button(miFrame, text='+', width=3, command=lambda:suma() )
BotonSumar.grid(row=5, column=4)




raiz.mainloop()

